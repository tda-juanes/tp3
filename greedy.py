# Escribir un algoritmo greedy que obtenga la solución óptima al problema.
# Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos.
import sys

def hitting_set(A, subsets):
    frequencies = {elem: 0 for elem in A}
    for subset in subsets:
        for elem in subset:
            frequencies[elem] += 1

    solution = []
    while subsets:
        e = max(frequencies, key=frequencies.get)

        i = 0
        while i < len(subsets):
            if e in subsets[i]:
                for other in subsets[i]:
                    frequencies[other] -= 1
                subsets.pop(i)
            else:
                i += 1

        del frequencies[e]
        solution.append(e)

    return solution

def parse_subsets(f):
    return [s.split(',') for s in map(str.strip, f) if s]

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] == '-':
        subsets = parse_subsets(sys.stdin)
    else:
        with open(sys.argv[1], "r") as f:
            subsets = parse_subsets(f)

    A = {elem for subset in subsets for elem in subset}
    sol = hitting_set(A, subsets)
    print(f"k = {len(sol)}")
    print(*sol, sep=", ")
