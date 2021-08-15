########################################
#  초기 풀이과정 시간 초과가 발생한다
# import sys
# num = int(sys.stdin.readline())
# numList= []
# countList =[]

# for i in range(num):
#     numList.append(list(map(int, input().split())))
# numList.sort()
# for i in range(num):
#     count = 0
#     for j in range(i,num):
#         if numList[i][1]<numList[j][0]:
#             numList[i][:] = numList[j][:]
#             count+=1
#     countList.append(count)
# print(max(countList)+1)
###################################################

# 두번째 풀이 과정 

import sys
num = int(sys.stdin.readline())
numList= []
countList =[]

for i in range(num):
    numList.append(list(map(int, input().split())))

numList = sorted(numList,key=lambda x: x[0] )
numList = sorted(numList,key=lambda x: x[1] )

end = 0
count = 0

for i, j in numList:
    if i >=end:
        count+=1
        end = j

print (count)
