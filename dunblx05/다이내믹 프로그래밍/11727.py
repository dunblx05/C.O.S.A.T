# 1 3 5 11...
# 1. n-1번째 경우의 수에서 2x1 직사각형을 붙인다.
# 2. n-2번째 경우의 수에서 2x2 직사각형을 붙인다.
# 3. n-2번째 경우의 수에서 1x2 직사각형을 2개 붙인다.

import sys

dp = [1,3]

for i in range(2, 1001):
    dp.append(dp[i-1] + 2 * dp[i-2])

n = int(sys.stdin.readline())

print(dp[n-1] % 10007)