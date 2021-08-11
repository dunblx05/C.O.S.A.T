# 1개 살 경우 -> price[1]
# 2개 살 경우 -> dp[1] + p[1], d[0] + p[2]
# 3개 살 경우 -> dp[2] + p[1], dp[1] + p[2], dp[0] + p[3]

import sys

n = int(sys.stdin.readline())
price = [0] + list(map(int, input().split()))

dp = [0 for _ in range(n + 1)]
dp[1] = price[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + price[j])

print(dp[n])