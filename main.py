import sys
import lib.backtracking
import lib.greedy

def parse_subsets(f):
    return [s.split(',') for s in map(str.strip, f) if s]

if __name__ == "__main__":
    match sys.argv:
        case [*_, '-'] | [_, '--approx' | '--greedy' | '--exact'] | [_]:
            subsets = parse_subsets(sys.stdin)
        case [*_, filename] if not filename.startswith('--'):
            with open(filename, "r") as f:
                subsets = parse_subsets(f)
        case _:
            print(
                "Usage:",
                f"    {sys.argv[0]} [--approx | --greedy | --exact] [filename]",
                file=sys.stderr, sep='\n'
            )
            exit(1)

    if '--approx' in sys.argv or '--greedy' in sys.argv:
        universal_set = set(sum(subsets, start=[]))
        sol = lib.greedy.hitting_set(universal_set, subsets)
    else:
        sol = lib.backtracking.hitting_set(subsets)
    print(f"k = {len(sol)}")
    print(*sol, sep=", ")
