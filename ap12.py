import sys

import cython
import numpy as np
from numba import jit


# cython.cdivision(True) disables validity checking for division by zero
# cython.locals() declares the types of variables as native
@cython.boundscheck(False)
@cython.cdivision(True)
@cython.locals(u=cython.int, r=cython.int, a=cython.int[10000], j=cython.int, i=cython.int)
def main():
    u = int(sys.argv[1])  # Get an input number from the command line
    r = np.random.randint(0, 10000)  # Get a random number 0 <= r < 10k
    mods = np.sum(np.arange(100000) % u) # 100k inner loop iterations, per outer loop iteration
    a = np.full(10000, mods + r)  # 10k outer loop iterations, 100k inner loop iterations, per outer loop iteration
    print(a[r])


if __name__ == '__main__':
    from ap12 import main
    main()