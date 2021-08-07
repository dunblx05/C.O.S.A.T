char = list(input())
char2 = list(input())
dp = [[0 for i in range(len(char)+1)]for i in range(len(char2)+1)]

for i in range(1,len(char)+1):
    for j in range(1,len(char2)+1):
        if char[i-1] == char2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])