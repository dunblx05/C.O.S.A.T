import sys
t = int(sys.stdin.readline())
for _ in range(t):
    k= int(sys.stdin.readline())
    sizes = list(map(int,sys.stdin.readline().split()))
    s = [0 for _ in range(k+1)]
    for i in range(1,k+1):
        s[i] = s[i-1]+sizes[i-1]
    dp = [[0 for _ in range(k+1)] for _ in range(k+1)]
    
    for i in range(2,k+1):
        for j in range(1,k+2-i):
            dp[j][i+j-1] = min([dp[j][j+k]+ dp[j+k+1][j+i-1]for k in range(i-1)])+(s[j+i-1] - s[j-1])
    print(dp[1][k])
