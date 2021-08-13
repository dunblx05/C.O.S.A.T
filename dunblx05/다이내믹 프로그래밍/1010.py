import sys
import math

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, input().split())
    comb = math.factorial(m) // (math.factorial(m - n) * math.factorial(n))
    print(comb)