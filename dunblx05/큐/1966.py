import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    importance = deque(list(map(int, sys.stdin.readline().split())))
    printlist = deque([0 for i in range(n)])
    printlist[m] = 1
    count = 0

    while True:
        if importance[0] == max(importance):
            count += 1

            if printlist[0] == 1:
                print(count)
                break
            else:
                importance.popleft()
                printlist.popleft()
        
        else:
            importance.append(importance.popleft())
            printlist.append(printlist.popleft())