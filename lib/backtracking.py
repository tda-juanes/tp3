import lib.greedy

def hitting_set_k(subsets, s_i, sol, k):
    if s_i == len(subsets):
        return sol

    for elem in subsets[s_i]:
        if elem in sol:
            return hitting_set_k(subsets, s_i + 1, sol, k)
    if len(sol) >= k:
        return

    # pruebo con todos los elementos del set actual
    for elem in subsets[s_i]:
        sol.append(elem)
        new_sol = hitting_set_k(subsets, s_i + 1, sol, k)
        if new_sol is not None:
            return new_sol
        sol.pop()

"""
Algoritmo por backtracking que encuentra la solución óptima al problema.
Encuentra una solución e intenta mejorarla hasta que no puede más.
"""
def hitting_set(A, subsets):
    # no es necesario, pero ayuda a encontrar la solucion mas rapido
    subsets.sort(key=len)

    best_solution = lib.greedy.hitting_set(A, subsets)

    while (sol := hitting_set_k(subsets, 0, [], len(best_solution) - 1)):
        best_solution = sol

    return best_solution

"""
Algoritmo por backtracking que encuentra la solución óptima al problema.
Itera desde un k mínimo hasta que encuentra una solución.
"""
def hitting_set_old(A, subsets):
    # no es necesario, pero ayuda a encontrar la solucion mas rapido
    subsets.sort(key=len)

    frequencies = {item: 0 for item in A}
    for subset in subsets:
        for item in subset:
            frequencies[item] += 1

    frequencies = sorted(frequencies.values(), reverse=True)
    S, k_min = len(subsets), 0
    while S > 0:
        S -= frequencies[k_min]
        k_min += 1

    for k in range(k_min, len(subsets)):
        sol = hitting_set_k(subsets, 0, [], k)
        if sol is not None:
            return sol

    return [subset[0] for subset in subsets]
