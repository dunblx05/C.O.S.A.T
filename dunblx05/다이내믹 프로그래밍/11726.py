# 1 2 3 5 8...

import sys

n = int(sys.stdin.readline())

dp = [1, 2]

for i in range(2, 1001):
    dp.append(dp[i-1] + dp[i-2])

print(dp[n-1] % 10007)