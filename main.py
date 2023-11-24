import sys

def parse_subsets(f):
    return [s.split(',') for s in map(str.strip, f) if s]

def run(subsets):
    # map strings to numbers for faster comparisons
    universal_set = list(set(sum(subsets, start=[])))
    subsets = [list(map(universal_set.index, subset)) for subset in subsets]
    sol = hitting_set(range(len(universal_set)), subsets)

    print(f"k = {len(sol)}")
    print(", ".join(universal_set[i] for i in sol))

if __name__ == "__main__":
    match sys.argv:
        case args if '--help' in args:
            print(
                "Usage:",
                f"    {sys.argv[0]} [--linear] [--approx] [filename]",
                file=sys.stderr, sep='\n'
            )
            exit(0)
        case [*_, filename] if not filename.startswith('-'):
            with open(filename, 'r') as f:
                subsets = parse_subsets(f)
        case _:
            subsets = parse_subsets(sys.stdin)

    if '--linear' in sys.argv:
        if '--approx' in sys.argv:
            from lib.linearprog import hitting_set_approx as hitting_set
        else:
            from lib.linearprog import hitting_set_exact as hitting_set
    elif '--approx' in sys.argv:
        from lib.greedy import hitting_set
    else:
        from lib.backtracking import hitting_set
    run(subsets)
