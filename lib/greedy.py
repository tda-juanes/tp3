# Escribir un algoritmo greedy que obtenga la solución óptima al problema.
# Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos.

def hitting_set(A, subsets):
    frequencies = {item: 0 for item in A}
    for subset in subsets:
        for item in subset:
            frequencies[item] += 1

    solution = []
    while subsets:
        item = max(frequencies, key=frequencies.get)

        subset_idx = 0
        while subset_idx < len(subsets):
            if item in subsets[subset_idx]:
                for other in subsets[subset_idx]:
                    frequencies[other] -= 1
                subsets.pop(subset_idx)
            else:
                subset_idx += 1

        del frequencies[item]
        solution.append(item)

    return solution
