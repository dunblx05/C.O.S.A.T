import sys

numlist = list(map(int, sys.stdin.readline().split()))
res = 0
for i in range(len(numlist)):
    res +=  pow(numlist[i], 2)

standnum = res % 10

print(standnum)