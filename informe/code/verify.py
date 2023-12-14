def is_hitting_set(A, B, C, k):
    if len(C) > k:
        return False
    for c in C:
        if c not in A:
            return False
    for Bi in B:
        for b in Bi:
            if b in C:
                break
        else:
            return False
    return True
