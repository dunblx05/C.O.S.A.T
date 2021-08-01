import sys
num = int(sys.stdin.readline())

stair = [0 for _ in range(num+3)]
numList=[0 for _ in range(num+3)]
for i in range(1,num+1):
    numList[i] = int(sys.stdin.readline().strip())

stair[1] = numList[1]
stair[2] = numList[1]+numList[2]
stair[3] = max(numList[1]+numList[3], numList[2]+numList[3])
for i in range(4,num+1):
    stair[i] = max(stair[i-3]+ numList[i-1] + numList[i],stair[i-2] + numList[i])
print(stair[num])