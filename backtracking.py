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
            return (True, sol, k)
        else:
            return backtracking_aux(subsets, s_i + 1, sol, k)

    if len(sol) >= k:
        return (False, sol, k)

    # caso borde, solo se da en 10_todos.txt
    if s_i == len(subsets) - 1:
        for elem in subsets[s_i]:
            if elem in sol:
                continue
            sol.append(elem)
            return (True, sol, k)

    # pruebo con todos los elementos del set actual
    for elem in subsets[s_i]:
        if elem in sol:
            continue
        n_sol = sol.copy()
        n_sol.append(elem)
        (valid, n_sol, k) = backtracking_aux(subsets, s_i + 1, n_sol, k)
        if valid:
            return (True, n_sol, k)

    return (False, sol, k)

def backtracking(subsets):
    initial_set = subsets[0]
    for i in range(1, len(subsets)+1):
        for j in initial_set:
            sol = [j]
            (valid, sol, k) = backtracking_aux(subsets, 1, sol, i)
            if valid:
                return (sol, k)

    return None

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
