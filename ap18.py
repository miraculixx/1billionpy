import sys
import random
import numpy as np

def compute(a, u, r):
    return a + np.sum(np.arange(100000) % u) + r

def main():
    u = int(sys.argv[1])         # Get an input number from the command line
    r = random.randint(0, 10000) # Get a random number 0 <= r < 10k
    a = np.zeros(10000)
    # Create an array of 10k elements
    # 10k outer loop iterations
    tasks = ((a[i], u, r) for i in np.arange(10000))
    # 100k inner loop iterations, per outer loop
    a = parallel(compute, tasks)
    print(a[r])                  # Print out a single element from the array

def parallel(fn, iterable):
    from multiprocessing import Pool
    with Pool(8) as p:
        return p.starmap(fn, iterable)

if __name__ == '__main__':
    main()

