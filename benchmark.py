import sys
import time
from random import randint, sample

from main import run

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
def benchmark(rango, amount_of_sets, set_size):
    for cant_elementos in rango:
        universal = list(range(cant_elementos))
        cant_subsets = int(cant_elementos*amount_of_sets)
        size = int(set_size*universal)
        subsets = [sample(universal, size) for _ in range(cant_subsets)]
        raise NotImplementedError
        timer_start = time.perf_counter()
        ### run hitting_set for (universal, subsets)
        timer_end = time.perf_counter()
        print(f'{cant_elementos},{timer_end - timer_start}')

def main():
    if not 1 < len(sys.argv) < 5:
        print(
            'Usage:\n'
            'python3 benchmark.py SET_AMOUNT SET_SIZE STOP\n'
            'python3 benchmark.py SET_AMOUNT SET_SIZE START STOP\n'
            'python3 benchmark.py SET_AMOUNT SET_SIZE START STOP STEP\n'
            "Example: 'python3 benchmark.py 0.2 0.05 100000 1000001 100000'\n",
            file=sys.stderr
        )
        exit(1)
    rango = range(*map(int, sys.argv[3:]))
    benchmark(rango, sys.argv(1), sys.argv(2))

if __name__ == '__main__':
    main()