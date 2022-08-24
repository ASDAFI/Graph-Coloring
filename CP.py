from typing import List, Tuple

from ortools.sat.python import cp_model

def create_model() -> cp_model.CpModel:
    return cp_model.CpModel()

def create_vars(model : cp_model.CpModel, nodes_count : int) -> List[cp_model.IntVar]:
    vars = []

    lower_bound = 0
    upper_bound = nodes_count

    for i in range(nodes_count):
        vars.append(model.NewIntVar(lower_bound, upper_bound, f'v{i}'))

    return vars

def add_constraints(model : cp_model.CpModel, vars : List[cp_model.IntVar], edges: List[Tuple[int]]) -> None:
    for edge in edges:
        model.Add(vars[edge[0]] != vars[edge[1]])

    return None

def create_objective_function(model : cp_model.CpModel, nodes_count : int,  vars : List[cp_model.IntVar]) -> cp_model.IntVar:

    lower_bound = 0
    upper_bound = nodes_count

    obj_var = model.NewIntVar(lower_bound, upper_bound, 'makespan')

    model.AddMaxEquality(obj_var, vars)
    model.Minimize(obj_var)

    return obj_var

def create_solver() -> cp_model.CpSolver:
    return cp_model.CpSolver()

def add_time_limit(solver : cp_model.CpSolver, time_limit : int) -> None:
    solver.parameters.max_time_in_seconds = time_limit
    return None


def solve(model : cp_model.CpModel, solver : cp_model.CpSolver):
    return solver.Solve(model)

def get_answer(solver: cp_model.CpSolver, vars : List[cp_model.IntVar]) -> List[int]:
    answer = []
    for var in vars:
        answer.append(solver.Value(var))
    return answer

def get_obj_value(solver: cp_model.CpSolver, obj_var : cp_model.IntVar) -> int:
    return solver.Value(obj_var)

def is_optimal(status):
    return status == cp_model.OPTIMAL
