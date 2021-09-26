import sys
import math

n, k  = map(int, sys.stdin.readline().split())

n_fac = math.factorial(n)
k_fac = math.factorial(k)
nk_fac = math.factorial(n-k)

res = int(n_fac / (k_fac * nk_fac))

print(res)