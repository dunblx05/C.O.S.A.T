import sys
import itertools

num = int(sys.stdin.readline())
number = [i for i in range(num)]
arr = [list(map(int, input().split()))for row in range(num)]
numList = range(num)
res = 1e9

for i in itertools.combinations(numList,num//2): #팀 나누기
    startm = list(i)
    linkm = list(set(number) - set(i))
# 팀에서 둘씩 조합 고려
    startCom = itertools.combinations(startm,2)
    linkCom = itertools.combinations(linkm,2)
# 팀에서 둘씩 조합에서 능력치 합 구하기
    startSum = 0
    for x,y, in startCom:
        startSum += arr[x][y]+arr[y][x]
    linkSum=0
    for x,y in linkCom:
        linkSum += arr[x][y] + arr[y][x]
# 두 팀의 능력치 차이 최소 구하기
    if (res > abs(startSum - linkSum)):
        res = abs(startSum - linkSum)

print(res)

