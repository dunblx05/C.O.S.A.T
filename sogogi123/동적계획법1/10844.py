num = int(input())
dp = [[0 for _ in range(10)]for j in range(101)]
for i in range(1,10):
    dp[1][i] = 1
for i in range(2,num+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp [i-1][1]
        elif j == 9:
            dp [i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp [i-1][j-1] + dp[i-1][j+1]
    
print(sum(dp[num])%1000000000)

#             0  1  2  3  4  5  6  7  8  9
# 자리수(1)   0  1  1  1  1  1  1  1  1  1
# 자리수(2)   1  1  2  2  2  2  2  2  2  1
# 자리수(3)   1  3  3  4  4  4  4  4  3  2
# 전 행의 대각선의 합을 구하는 점화식으로 구할 수 있다.