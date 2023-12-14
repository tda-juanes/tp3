import sys
import time
import random

import lib.linearprog
import lib.backtracking
import lib.greedy

'''
Receives a range of natural numbers and for each n in the range
outputs the size of the optimal solution, and the sizes of the approximate
solutions using the greedy and relaxed linear programming algorithms
The amount of sets is given by amount_of_sets*n, with 0<amount_of_sets<1.
The size of each subset is given by set_size*n, with 0<set_size<1.
Output has the following format:
"""
n_1,k_min_1,k_greedy_1,k_linear_1,linear2_1
n_2,k_min_2,k_greedy_2,k_linear_2,linear2_2
...
n_i,k_min_i,k_greedy_i,k_linear_i,linear2_i
"""
'''
def test_quality(r, rango, amount_of_sets, set_size, output):
    for cant_elementos in rango:
        universal = range(cant_elementos)
        cant_subsets = int(cant_elementos*amount_of_sets)
        size = int(set_size*cant_elementos)
        subsets = [r.sample(universal, size) for _ in range(cant_subsets)]

        bt = len(lib.backtracking.hitting_set(universal, subsets))
        gr = len(lib.greedy.hitting_set(universal, subsets))
        lp = len(lib.linearprog.hitting_set_approx(universal, subsets))
        l2 = len(lib.linearprog.hitting_set_approx2(universal, subsets))

        print(f'{cant_elementos},{bt},{gr},{lp},{l2}', file=output)

def main():
    if not 3 < len(sys.argv) < 6:
        exit(
            'Usage:\n'
            f'  python3 {sys.argv[0]} SET_AMOUNT SET_SIZE STOP\n'
            f'  python3 {sys.argv[0]} SET_AMOUNT SET_SIZE START STOP\n'
            f'  python3 {sys.argv[0]} SET_AMOUNT SET_SIZE START STOP STEP\n'
            f'    example: `python3 {sys.argv[0]} 0.2 0.05 100 150 5`'
        )

    seed = random.randbytes(16)
    args = list(map(eval, sys.argv[1:]))
    rango = range(*args[2:])

    with open('quality.csv', 'a') as f:
        test_quality(random.Random(seed), rango, args[0], args[1], f)

if __name__ == '__main__':
    main()
