# 1 1 2 3 5 8 13....

import sys

dp = [1,1,2]

for i in range(3, 91):
    dp.append(dp[i-2] + dp[i-1])

n = int(sys.stdin.readline())

print(dp[n-1])