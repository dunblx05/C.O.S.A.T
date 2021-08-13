#    0 1 2  3  4  5  6  7  8  9
# 1  1 1 1  1  1  1  1  1  1  1 -> 10
# 2  1 2 3  4  5  6  7  8  9 10 -> 55
# 3  1 3 6 10 15 21 28 36 45 55 -> 220

import sys

n = int(sys.stdin.readline())

dp = [[1 for _ in range(10)] for _ in range(n)]

for i in range(1, n):
    for j in range(1, 10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(sum(dp[n-1]) % 10007)