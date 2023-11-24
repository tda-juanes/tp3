import sys
import time
import random

from lib.backtracking import hitting_set as hsb
from lib.linearprog import hitting_set_exact as hslp
# from lib.linearprog import hitting_set_approx as hslpr
# from lib.greedy import hitting_set as hsg

'''
Receives a range of natural numbers and for each n in the range
outputs the time taken to solve the hitting set problem for n elements.
The amount of sets is given by amount_of_sets*n, with 0<amount_of_sets<1.
The size of each subset is given by set_size*n, with 0<set_size<1.
Output has the following format:
"""
n_1,time_taken_1
n_2,time_taken_2
...
n_i,time_taken_i
"""
'''
def benchmark(r, hitting_set, rango, amount_of_sets, set_size, output):
    for cant_elementos in rango:
        universal = range(cant_elementos)
        cant_subsets = int(cant_elementos*amount_of_sets)
        size = int(set_size*cant_elementos)
        subsets = [r.sample(universal, size) for _ in range(cant_subsets)]

        timer_start = time.perf_counter()
        hitting_set(universal, subsets)
        timer_end = time.perf_counter()

        print(f'{cant_elementos},{timer_end - timer_start}', file=output)
        print(cant_elementos)

def main():
    if not 3 < len(sys.argv) < 6:
        print(
            'Usage:\n'
            'python3 benchmark.py SET_AMOUNT SET_SIZE STOP\n'
            'python3 benchmark.py SET_AMOUNT SET_SIZE START STOP\n'
            'python3 benchmark.py SET_AMOUNT SET_SIZE START STOP STEP\n'
            "Example: 'python3 benchmark.py 0.2 0.05 100000 1000001 100000'\n",
            file=sys.stderr
        )
        exit(1)

    seed = random.randbytes(16)
    args = list(map(eval, sys.argv[1:]))
    rango = range(*args[2:])

    funcs = [hsb, hslp]
    # funcs = [hsg, hslpr]
    files = ['benchmarks/backtracking.csv', 'benchmarks/linear_prog.csv']
    # files = ['benchmarks/greedy.csv', 'benchmarks/linear_prog_relaxed.csv']

    for func, file in zip(funcs, files):
        with open(file, 'w') as f:
            benchmark(random.Random(seed), func, rango, args[0], args[1], f)

if __name__ == '__main__':
    main()
