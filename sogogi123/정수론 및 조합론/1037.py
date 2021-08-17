import sys
num = int(sys.stdin.readline())
factors = list(map(int,sys.stdin.readline().split()))
factors.sort()
print(factors[0]*factors[-1])