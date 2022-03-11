import sys
import heapq
n = int(sys.stdin.readline())
xi = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x== 0:
        if len(xi)==0:
            print(0)
        else:
            print(xi[0])
            heapq.heappop(xi)
    else:
        heapq.heappush(xi, x)
        
            
