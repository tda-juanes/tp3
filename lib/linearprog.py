import pulp
from pulp import LpVariable, LpProblem, lpSum, LpMinimize

def hitting_set(A, subsets, variable_cat):
    binary_vars = {item: LpVariable(item, cat=variable_cat) for item in A}
    problem = LpProblem('Hitting Set', LpMinimize)
    for subset in subsets:
        subset_items = list(map(binary_vars.get, subset))
        problem += lpSum(subset_items) >= 1
    problem += lpSum(list(binary_vars.values()))
    problem.solve()
    return {item.getName(): pulp.value(item) for item in binary_vars.values()}

"""
Algoritmo por programación lineal entera que obtiene la solución óptima al problema.
"""
def hitting_set_exact(A, subsets):
    result = hitting_set(A, subsets, 'Binary')
    return [item for item, value in result if value > 0]

"""
Algoritmo por programación lineal que obtiene una solución aproximada al problema.
"""
def hitting_set_approx(A, subsets):
    result = hitting_set(A, subsets, 'Integer')
    # todo!()
    raise NotImplemented
