n, max_w = map(int,input().split())
dp=[[0 for i in range(max_w+1)] for i in range(n+1)]
w =[0]
v=[0]
for i in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

for i in range(1,n+1):
    for j in range(1,max_w+1):
        if w[i]<=j:
            dp[i][j] = max(v[i]+dp[i-1][j-w[i]],dp[i-1][j]) 
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])