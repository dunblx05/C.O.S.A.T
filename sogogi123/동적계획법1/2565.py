# 예제입력
# 8
# 1 8
# 3 9
# 2 2
# 4 1
# 6 4
# 10 10
# 9 7
# 7 6

# 예제 출력
# 3

import sys
num = int(sys.stdin.readline())
numList=[]
for i in range(num):
    numList.append(list(map(int,input().split())))
dp = [0 for i in range(num)]

numList.sort()

for i in range(num):
    for j in range(num):
        if dp[i]<dp[j]\
            and numList[i][1]>numList[j][1]:
            dp[i]= dp[j]
    dp[i]+=1

print(num-max(dp))

#