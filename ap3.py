import sys
import random
u = int(sys.argv[1])         # Get an input number from the command line
r = 0 # random.randint(0, 10000) # Get a random number 0 <= r < 10k
a = [sum(i + u for j in range(100000)) + r
     for i in range(10000)] # 10k outer loop iterations, 100k inner loop iterations, per outer loop iteration
print(a[r])
