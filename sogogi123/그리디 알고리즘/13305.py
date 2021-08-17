import sys
num = int(sys.stdin.readline())
dist_list = list(map(int, sys.stdin.readline().split()))
gas_list = list(map(int, sys.stdin.readline().split()))
res = 0
for i in range(num-1):
    if gas_list[i] == min(gas_list[:-2]):
        res += gas_list[i] *sum(dist_list[i:])
        break
    else:
        res += gas_list[i]*dist_list[i]
print(res)

