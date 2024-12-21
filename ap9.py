import sys

import numpy as np


def main():
    u = int(sys.argv[1])  # Get an input number from the command line
    r = np.random.randint(0, 10000)  # Get a random number 0 <= r < 10k
    mods = np.sum(np.arange(100000) % u) # 100k inner loop iterations, per outer loop iteration
    a = np.full(10000, mods + r)  # 10k outer loop iterations, 100k inner loop iterations, per outer loop iteration
    print(a[r])
main()