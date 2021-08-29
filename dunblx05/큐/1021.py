import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
order = list(map(int, sys.stdin.readline().split()))
queue = deque([i for i in range(1, n + 1)])
count = 0

for i in range(m):
    
    while True:
        if queue[0] == order[i]:
            queue.popleft()
            break
        else:
            if queue.index(order[i]) < len(queue) / 2:
                while queue[0] != order[i]:
                    queue.append(queue.popleft())
                    count += 1
            else:
                while queue[0] != order[i]:
                    queue.appendleft(queue.pop())
                    count += 1
                    
print(count)