import sys
num = int(sys.stdin.readline())
n = []
res = []
for i in range(num):
    nums = list(map(int, input().split()))
    n.append(nums)

for i in range(1,num):
    for j in range(i+1):
        if j==0:
            n[i][j]= n[i-1][j]+n[i][j]
        elif j ==i:
            n[i][j] = n[i-1][j-1] +n[i][j]
        else:
            n[i][j] = max(n[i-1][j-1],n[i-1][j])+ n[i][j]
for i in range(num):
    res.append(n[num-1][i])
print(max(res))       