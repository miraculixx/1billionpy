import random
import sys

import cython


# cython.cdivision(True) disables validity checking for division by zero
# cython.locals() declares the types of variables as native
@cython.boundscheck(False)
@cython.cdivision(True)
@cython.locals(u=cython.int, r=cython.int, a=cython.int[10000], j=cython.int, i=cython.int)
def main():
    u = int(sys.argv[1])  # Get an input number from the command line
    r = random.randint(0, 10000)  # Get a random number 0 <= r < 10k
    mods = sum([j % u for j in range(100000)])  # 100k inner loop iterations, per outer loop iteration
    a = [mods + r for i in range(10000)]  # 10k outer loop iterations, 100k inner loop iterations, per outer loop iteration
    print(a[r])


if __name__ == '__main__':
    from ap13 import main
    main()