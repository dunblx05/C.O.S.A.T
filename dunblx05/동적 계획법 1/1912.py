import sys

n = int(sys.stdin.readline())

numlist = list(map(int,input().split()))

sum = [numlist[0]]

for i in range(1, n):
    sum.append(max(sum[i-1] + numlist[i], numlist[i]))

print(max(sum))