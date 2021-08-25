import sys
from collections import deque
num = int(sys.stdin.readline())
queue = deque()
for i in range(1,num+1):
    queue.append(i)
while len(queue)>1:
    queue.popleft()
    queue.rotate(-1)

print(queue[0])

