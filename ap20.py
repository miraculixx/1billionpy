import random
import sys

import numpy as np
from numba import jit, void, int32, prange


@jit(void(int32), cache=True, boundscheck=False, fastmath=True, nopython=True)
def main(u):
    r = random.randint(0, 10000) # Get a random number 0 <= r < 10k
    a = np.zeros(10000, dtype=np.int32)  # Create an array of 10k elements
    # Perform the operation for each element in a
    for i in prange(10000):
        a[i] += np.sum(np.arange(100000) % u) + r
    print(a[r])                  # Print out a single element from the array

if __name__ == '__main__':
    u = int(sys.argv[1])  # Get an input number from the command line
    main(u)