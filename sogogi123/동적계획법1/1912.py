import sys
num = int(sys.stdin.readline())
numList = list(map(int,input().split()))

dp = [0 for i in range(num)]
dp[0] = numList[0]
for i in range(1,num):
    dp[i] = max(numList[i]+dp[i-1], numList[i])
print(max(dp))
