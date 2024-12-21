from itertools import starmap
import sys
import random
import numpy as np
from numba import njit

def compute(a, u, r):
    return a + np.sum(np.arange(100000) % u) + r


@njit
def main():
    u = int(sys.argv[1])         # Get an input number from the command line
    r = random.randint(0, 10000) # Get a random number 0 <= r < 10k
    a = [0] * 10000
    # Create an array of 10k elements
    # 10k outer loop iterations
    tasks = ((a[i], u, r) for i in range(10000))
    # 100k inner loop iterations, per outer loop
    a[:] = starmap(compute, tasks)
    print(a[r])                  # Print out a single element from the array

if __name__ == '__main__':
    main()
