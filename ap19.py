import sys
import random
import numpy as np

def main():
    u = int(sys.argv[1])         # Get an input number from the command line
    r = random.randint(0, 10000) # Get a random number 0 <= r < 10k
    a = np.zeros(10000, dtype=np.int32)  # Create an array of 10k elements

    # Perform the operation for each element in a
    for i in range(10000):
        # Instead of using a lambda, we directly compute the sum in the loop
        a[i] += np.sum(np.arange(100000) % u) + r

    print(a[r])                  # Print out a single element from the array

if __name__ == '__main__':
    main()