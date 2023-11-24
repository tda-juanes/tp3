import sys
import time
import random

import lib.linearprog

'''
Receives a range of natural numbers and for each n in the range
outputs the size of the approximated solution divided by the size of the
optimal solution for the hitting set problem for n elements.
The amount of sets is given by amount_of_sets*n, with 0<amount_of_sets<1.
The size of each subset is given by set_size.
Output has the following format:
"""
n_1,A(I1)/z(I1)
n_2,A(I2)/z(I2)
...
n_i,A(Ii)/z(Ii)
"""
'''
def upper_bound(r, rango, amount_of_sets, set_size, output):
    for cant_elementos in rango:
        universal = range(cant_elementos)
        cant_subsets = int(cant_elementos*amount_of_sets)
        subsets = [r.sample(universal, set_size) for _ in range(cant_subsets)]

        b = set_size
        # k_min = len(lib.linearprog.hitting_set_exact(universal, subsets))
        # k_approx = len(lib.linearprog.hitting_set_relaxed(universal, subsets))
        values = lib.linearprog.hitting_set(
                universal, subsets,
                cat='Continuous',
                lowBound=0, upBound=1
        )
        k_min = k_approx = 0
        for value in values:
            if value >= 1/b:
                k_approx += 1
            k_min += value


        print(f'{cant_elementos},{k_approx/k_min},{b}', file=output)

def main():
    if not 3 < len(sys.argv) < 6:
        print(
            'Usage:\n'
            'python3 relaxation.py SET_AMOUNT SET_SIZE STOP\n'
            'python3 relaxation.py SET_AMOUNT SET_SIZE START STOP\n'
            'python3 relaxation.py SET_AMOUNT SET_SIZE START STOP STEP\n'
            "Example: 'python3 relaxation.py 0.2 20 100000 1000001 100000'\n",
            file=sys.stderr
        )
        exit(1)

    seed = random.randbytes(16)
    args = list(map(eval, sys.argv[1:]))
    rango = range(*args[2:])

    with open('relaxation.csv', 'a') as f:
        upper_bound(random.Random(seed), rango, args[0], args[1], f)

if __name__ == '__main__':
    main()
