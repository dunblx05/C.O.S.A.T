import sys

n, k = map(int,input().split())

dp = [0 for _ in range(k + 1)]
dp [0] = 1

coin = []

for i in range(n):
    coin.append(int(input()))

for i in coin:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j-i]

print(dp[k])