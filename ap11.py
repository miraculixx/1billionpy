import random
import sys

import numpy as np
from numba import jit, int32, void

@jit(void(int32), cache=True, boundscheck=False, fastmath=True, nopython=True, parallel=True)
def main(u):
    r = random.randint(0, 10000)  # Get a random number 0 <= r < 10k
    a = np.zeros(10000)
    for i in range(10000):  # 10k outer loop iterations
        for j in range(100000):  # 100k inner loop iterations, per outer loop iteration
            a[i] += j % u  # Simple sum
        a[i] += r  # Add a random value to each element in array
    print(a[r])


u = int(sys.argv[1])  # Get an input number from the command line
main(u)
