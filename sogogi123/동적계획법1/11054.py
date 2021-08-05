# 예제입력
# 10
# 1 5 2 1 4 3 4 5 2 1

# 예제 출력
# 7

num = int(input())
numList =list(map(int, input().split()))
dp =[0 for i in range(num)]
rdp = [0 for i in range(num)]
sdp = [0 for i in range(num)]
for i in range(num):
    for j in range(num):
        if dp[i]<dp[j] and numList[i]>numList[j]:
            dp[i]= dp[j]
    dp[i]+=1

for i in range(num-1,-1,-1):
    for j in range(num-1,-1,-1):
        if rdp[i]<rdp[j] and numList[j]<numList[i]:
            rdp[i]=rdp[j]
    rdp[i] += 1


for i in range(num):
    sdp[i] = rdp[i]+dp[i]

print(max(sdp)-1)