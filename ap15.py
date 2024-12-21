from itertools import starmap
import sys
import random
import numpy as np

def main():
    u = int(sys.argv[1])         # Get an input number from the command line
    r = random.randint(0, 10000) # Get a random number 0 <= r < 10k
    a = np.zeros(10000)
    # Create an array of 10k elements
    # 10k outer loop iterations
    tasks = ((a[i], u, r) for i in np.arange(10000))
    # 100k inner loop iterations, per outer loop
    compute = lambda a, u, r: a + np.sum(np.arange(100000) % u) + r
    a = np.fromiter(starmap(compute, tasks), np.int32)
    print(a[r])                  # Print out a single element from the array

if __name__ == '__main__':
    main()
