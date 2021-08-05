# 예제입력
# 6
# 10 20 10 30 20 50
# 예제출력
# 4
# import sys
# num = int(sys.stdin.readline())
# numList = list(map(int,(input().split())))

# arr=[]
# arr.append(numList[0])
# for i in range(1,num):
#     if arr[len(arr)-1]<numList[i]:
#         arr.append(numList[i])

# print(len(arr))


# 다시 풀이 dp? 이용
import sys
num = int(sys.stdin.readline())
numList = list(map(int,(input().split())))
dp =[0 for i in range(num)]

for i in range(num):
    for j in range(num):
        if dp[i]<dp[j] and numList[j]<numList[i]:#바이토닉 수열 구하는 법 dp 수열 끼리 비교하여 순서를 찾아내고 numList 수열끼리 비교하여 크기에 따라 dp 수열을 정하였다.
            dp[i]=dp[j]
        
    dp[i] +=1

print(max(dp))