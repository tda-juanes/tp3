def hitting_set(A, subsets):
    frequencies = {item: 0 for item in A}
    for subset in subsets:
        for item in subset:
            frequencies[item] += 1

    solution = []
    missing = list(subsets)
    while missing:
        item = max(frequencies, key=frequencies.get)

        subset_idx = 0
        while subset_idx < len(missing):
            if item in missing[subset_idx]:
                for other in missing[subset_idx]:
                    frequencies[other] -= 1
                missing.pop(subset_idx)
            else:
                subset_idx += 1

        del frequencies[item]
        solution.append(item)

    return solution
