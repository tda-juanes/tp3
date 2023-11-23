import pulp

def hitting_set(A, subsets, **kwargs):
    variables = {item: pulp.LpVariable(f'Y{i}', **kwargs) for i, item in enumerate(A, 1)}
    problem = pulp.LpProblem('Hitting_Set', pulp.LpMinimize)

    for subset in subsets:
        subset_items = list(map(variables.get, subset))
        problem += pulp.lpSum(subset_items) >= 1

    problem += pulp.lpSum(list(variables.values()))
    problem.solve()

    return {item: pulp.value(var) for item, var in variables.items()}

"""
Algoritmo por programación lineal entera que obtiene la solución óptima al
problema.
"""
def hitting_set_exact(A, subsets):
    result = hitting_set(A, subsets, cat='Binary')
    return [item for (item, value) in result.items() if value > 0]

"""
Algoritmo por programación lineal que obtiene una solución aproximada al
problema.
"""
def hitting_set_approx(A, subsets):
    b = max(map(len, subsets))
    result = hitting_set(A, subsets, cat='Continuous', lowBound=0, upBound=1)
    return [item for (item, value) in result.items() if value >= 1/b]
