import sys

def parse_subsets(f):
    return [s.split(',') for s in map(str.strip, f) if s]

if __name__ == "__main__":
    match sys.argv:
        case [*_, filename] if not filename.startswith('-'):
            with open(filename, 'r') as f:
                subsets = parse_subsets(f)
        case _:
            subsets = parse_subsets(sys.stdin)
        # case _:
        #     print(
        #         "Usage:",
        #         f"    {sys.argv[0]} [--linear] [--approx] [filename]",
        #         file=sys.stderr, sep='\n'
        #     )
        #     exit(1)

    universal_set = set(sum(subsets, start=[]))

    if '--linear' in sys.argv:
        if '--approx' in sys.argv:
            from lib.linearprog import hitting_set_approx as hitting_set
        else:
            from lib.linearprog import hitting_set_exact as hitting_set
    elif '--approx' in sys.argv:
        from lib.greedy import hitting_set
    else:
        from lib.backtracking import hitting_set

    sol = hitting_set(universal_set, subsets)
    print(f"k = {len(sol)}")
    print(*sol, sep=", ")
