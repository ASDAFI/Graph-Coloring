#!/usr/bin/python
# -*- coding: utf-8 -*-
import CP as cp
from typing import List, Tuple






def solve_it(edges : List[Tuple[int]], nodes_count: int):


    # every node has its own color
    model = cp.create_model()
    vars = cp.create_vars(model, nodes_count)

    cp.add_constraints(model, vars, edges)
    obj_var = cp.create_objective_function(model, nodes_count, vars)

    solver = cp.create_solver()
    cp.add_time_limit(solver, 300)

    status = cp.solve(model, solver)

    answer = cp.get_answer(solver, vars)
    obj_value = cp.get_obj_value(solver, obj_var)
    is_optimal = cp.is_optimal(status) * 1

    return answer, obj_value, is_optimal
