import sys

n = int(sys.stdin.readline())

arr = list(map(int, input().split()))

dp = [1 for i in range(n)]
dp_r = [1 for i in range(n)]
res = []

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i - 1, -1):
        if arr[i] > arr[j]:
            dp_r[i] = max(dp_r[i], dp_r[j] + 1)

for i in range(n):
    res.append(dp[i] + dp_r[i])

print(max(res) - 1)