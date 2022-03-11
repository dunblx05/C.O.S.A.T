import sys
import heapq
n = int(sys.stdin.readline())

leftary = []
rightary = []
#  좌우 리스트의 크기가 같도록 만들어 준다.
for _ in range(n):
    x = int(sys.stdin.readline())
    if len(leftary) ==len(rightary):
        heapq.heappush(leftary,-x)
    else:
        heapq.heappush(rightary,x)

    # 좌우 리스트에 항이 있는 경우 크기 비교를 하여 작은 값이 왼쪽 리스트에 오도록 한다
    if len(rightary)>=1 and len(leftary) >=1 and rightary[0]<-1*leftary[0]:
            right = heapq.heappop(rightary)
            left = heapq.heappop(leftary)*-1
            heapq.heappush(leftary,right*-1)
            heapq.heappush(rightary,left)
        
    print(-1*leftary[0])

