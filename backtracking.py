# Escribir un algoritmo que, por backtracking, obtenga la solución óptima al problema.
# Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos.
import sys

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
        return None

    # pruebo con todos los elementos del set actual
    for elem in subsets[s_i]:
        sol.append(elem)
        n_sol = hitting_set_k(subsets, s_i + 1, sol, k)
        if n_sol is not None:
            return n_sol
        sol.pop()

    return None

def hitting_set(subsets):
    for i in range(1, len(subsets)):
        sol = hitting_set_k(subsets, 0, [], i)
        if sol is not None:
            return sol, i

    return [subset[0] for subset in subsets], len(subsets)

def parse_subsets(f):
    return [s.split(',') for line in f for s in [line.strip()] if s]

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] == '-':
        subsets = parse_subsets(sys.stdin)
    else:
        with open(sys.argv[1], "r") as f:
            subsets = parse_subsets(f)

    # no es necesario, pero ayuda a encontrar la solucion mas rapido
    subsets.sort(key=len)

    sol, k = hitting_set(subsets)
    print(f"{k = }")
    print(*sol, sep=", ")
