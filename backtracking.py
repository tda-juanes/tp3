# Escribir un algoritmo que, por backtracking, obtenga la solución óptima al problema.
# Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos.
import sys

def intersects(subset, sol):
    for elem in subset:
        if elem in sol:
            return True
    return False

def backtracking_aux(subsets, s_i, sol, k):
    if intersects(subsets[s_i], sol):
        if s_i == len(subsets) - 1:
            return sol
        else:
            return backtracking_aux(subsets, s_i + 1, sol, k)

    if len(sol) >= k:
        return None

    # pruebo con todos los elementos del set actual
    for elem in subsets[s_i]:
        if elem in sol:
            continue
        sol.append(elem)
        n_sol = backtracking_aux(subsets, s_i + 1, sol, k)
        if n_sol is not None:
            return n_sol
        sol.pop()

    return None

def backtracking(subsets):
    if not subsets:
        return subsets, 0

    for i in range(len(subsets)):
        sol = backtracking_aux(subsets, 0, [], i)
        if sol is not None:
            return sol, i

    return [subset[0] for subset in subsets], len(subsets)

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 backtracking.py <archivo>")
        return

    file = open(sys.argv[1], "r")

    subsets = []
    for line in file.readlines():
        subsets.append(line.strip().split(","))
    subsets = sorted(subsets, key=lambda x: len(x)) # no es necesario,
                                                    # pero ayuda a encontrar
                                                    # la solucion mas rapido

    sol = backtracking(subsets)
    print(sol)

main()
