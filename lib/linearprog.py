import pulp

def hitting_set(A, subsets, category):
    binary_vars = {item: pulp.LpVariable(f'Y{i}', cat=category) for i, item in enumerate(A, 1)}
    problem = pulp.LpProblem('Hitting_Set', pulp.LpMinimize)

    for subset in subsets:
        subset_items = list(map(binary_vars.get, subset))
        problem += pulp.lpSum(subset_items) >= 1

    problem += pulp.lpSum(list(binary_vars.values()))
    problem.solve()

    return {item: pulp.value(var) for item, var in binary_vars.items()}

"""
Algoritmo por programación lineal entera que obtiene la solución óptima al
problema.
"""
def hitting_set_exact(A, subsets):
    result = hitting_set(A, subsets, 'Binary')
    return [item for (item, value) in result.items() if value > 0]

"""
Algoritmo por programación lineal que obtiene una solución aproximada al
problema.
"""
def hitting_set_approx(A, subsets):
    b = max(map(len, subsets))
    result = hitting_set(A, subsets, 'Continuous')
    return [item for (item, value) in result.items() if value >= 1/b]
