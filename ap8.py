import random
import sys


def main():
    u = int(sys.argv[1])  # Get an input number from the command line
    r = 15 #random.randint(0, 10000)  # Get a random number 0 <= r < 10k
    mods = sum(j % u for j in range(100000)) # 100k inner loop iterations, per outer loop iteration
    a = [mods + r for i in range(10000)]  # 10k outer loop iterations, 100k inner loop iterations, per outer loop iteration
    print(a[r])

main()