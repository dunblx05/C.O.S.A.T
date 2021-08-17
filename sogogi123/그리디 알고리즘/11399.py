import sys
num = int(sys.stdin.readline())
num_list = list(map(int,input().split()))
res = 0
num_list.sort()
for i in range(num+1):
    res += sum(num_list[:i])

print(res)