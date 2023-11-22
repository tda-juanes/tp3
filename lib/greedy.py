# Escribir un algoritmo greedy que obtenga la solución óptima al problema.
# Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos.

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
