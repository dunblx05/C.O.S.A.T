import sys

n = int(sys.stdin.readline())

elec1 = [[0 for i in range(2)] for i in range(n)]
dp = [1 for i in range(n)]

for i in range(n):
    elec1[i] = list(map(int, input().split()))

# 첫번째 전깃줄 위치를 기준으로 정렬
elec1.sort(key = lambda x:x[0])

for i in range(n):
    for j in range(i):
        if elec1[i][1] > elec1[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))