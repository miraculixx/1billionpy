import sys
import random
from array import array

u = int(sys.argv[1])         # Get an input number from the command line
r = 0 # random.randint(0, 10000) # Get a random number 0 <= r < 10k
ia = list(range(10000))
ib = list(range(100000))
a = list(map(lambda i: sum(i + u for j in ib) + r, ia)) # 10k outer loop iterations, 100k inner loop iterations, per outer loop iteration
print(a[r], len(a))