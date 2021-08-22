import sys
num = int(sys.stdin.readline())
dist_list = list(map(int, sys.stdin.readline().split()))
gas_list = list(map(int, sys.stdin.readline().split()))
res = 0
minV = sys.maxsize

for i in range(num-1):
    if i ==0:
        res += gas_list[0] * dist_list[0]
        minV = min(minV,gas_list[i])
    else:
        minV = min(minV,gas_list[i])
        res += minV*dist_list[i]
print(res)
