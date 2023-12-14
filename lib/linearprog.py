import pulp

def hitting_set(A, subsets, **kwargs):
    variables = [pulp.LpVariable(f'Y{item}', **kwargs) for item in A]
    problem = pulp.LpProblem('Hitting_Set', pulp.LpMinimize)

    for subset in subsets:
        subset_items = [variables[item] for item in subset]
        problem += pulp.lpSum(subset_items) >= 1

    problem += pulp.lpSum(variables)
    problem.solve()

    return map(pulp.value, variables)

"""
Algoritmo por programación lineal entera que obtiene la solución óptima al
problema.
"""
def hitting_set_exact(A, subsets):
    result = hitting_set(A, subsets, cat='Binary')
    return [item for (item, value) in enumerate(result) if value > 0]

"""
Algoritmo por programación lineal que obtiene una solución aproximada al
problema.
"""
def hitting_set_approx(A, subsets):
    b = max(map(len, subsets))
    result = hitting_set(A, subsets, cat='Continuous', lowBound=0, upBound=1)
    return [item for (item, value) in enumerate(result) if value >= 1/b]

"""
Algoritmo por programación lineal que obtiene una solución aproximada al
problema.
Luego de calcular los valores de los elementos, toma el elemento de mayor valor
de cada subset (priorizando elementos que ya fueron utilizados), y con ellos
genera el resultado.
"""
def hitting_set_approx2(A, subsets):
    b = max(map(len, subsets))
    result = hitting_set(A, subsets, cat='Continuous', lowBound=0, upBound=1)
    result = list(result)
    ret = set()
    for subset in subsets:
        _, item = max((result[item], item) for item in subset)
        # prioriza elementos que ya estan en el resultado
        result[item] = float('inf')
        ret.add(item)
    return list(ret)
