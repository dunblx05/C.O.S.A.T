# 6 10 13 9 8 1
# dp[0] = wine[0] = 6
# dp[1] = wine[0] + wine[1] = 16
# dp[2] = max(wine[0] + wine[1], wine[1] + wine[2], wine[0] + wine[2]) = 23
# dp[3] = max(wine[0] + wine[1] + wine[3], wine[0] + wine[2] + wine[3], wine[1] + wine[2])

import sys

n = int(sys.stdin.readline())

wine = []
dp = []
for i in range(n):
    wine.append(int(input()))

if n == 1:
    print(wine[0])

elif n == 2:
    print(wine[0] + wine[1])

elif n == 3:
    print(max(wine[0] + wine[1], wine[1] + wine[2], wine[0] + wine[2]))
    
else:
    dp.append(wine[0])
    dp.append(wine[0] + wine[1])
    dp.append(max(dp[1], wine[1] + wine[2], wine[0] + wine[2]))

    for i in range(3,n):
        # i번째 와인을 마시지 않는 경우, i번째 와인을 마시고 전전까지의 최대양
        # i번째와 전번째 와인을 마시고 전전전까지의 최대양
        dp.append(max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i]))

    print(dp[n-1])