def hitting_set(A, subsets):
    frequencies = [0] * len(A)
    for subset in subsets:
        for item in subset:
            frequencies[item] += 1

    solution = []
    missing = list(subsets)
    while missing:
        item, _ = max(enumerate(frequencies), key=lambda t: t[1])

        subset_idx = 0
        while subset_idx < len(missing):
            if item in missing[subset_idx]:
                for other in missing[subset_idx]:
                    frequencies[other] -= 1
                missing.pop(subset_idx)
            else:
                subset_idx += 1

        solution.append(item)

    return solution
