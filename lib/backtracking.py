import lib.greedy

def intersects(subset, sol):
    for elem in subset:
        if elem in sol:
            return True
    return False

def hitting_set_k(subsets, s_i, sol, k):
    if intersects(subsets[s_i], sol):
        if s_i == len(subsets) - 1:
            return sol
        else:
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
"""
def hitting_set(A, subsets):
    # no es necesario, pero ayuda a encontrar la solucion mas rapido
    subsets.sort(key=len)

    best_solution = lib.greedy.hitting_set(A, subsets)

    while (sol := hitting_set_k(subsets, 0, [], len(best_solution) - 1)):
        best_solution = sol

    return best_solution
