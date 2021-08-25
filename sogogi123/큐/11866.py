import sys
from collections import deque
a,b = map(int, sys.stdin.readline().split())
queue =deque()
for i in range(1,a +1):
    queue.append(i)
print('<', end='')
for i in range(a):
    for j in range(b-1):
        queue.append(queue[0])
        queue.popleft()
    print(queue.popleft(), end='')
    if queue:
        print(', ', end='')
print('>')   