# Escribir un algoritmo que, por backtracking, obtenga la solución óptima al problema.
# Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos.
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

def hitting_set(subsets):
    # no es necesario, pero ayuda a encontrar la solucion mas rapido
    subsets.sort(key=len)

    for k in range(1, len(subsets)):
        sol = hitting_set_k(subsets, 0, [], k)
        if sol is not None:
            return sol

    return [subset[0] for subset in subsets]
