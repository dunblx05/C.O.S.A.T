N, K = map(int,input().split())
numList = []
res = []

for i in range(N):
    numList.append(int(input()))
for i in range(N-1,-1,-1):
    res.append(K//numList[i])
    K =K% numList[i]
print(sum(res))
