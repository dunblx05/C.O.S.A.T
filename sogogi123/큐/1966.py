import sys
from collections import deque

num = int(sys.stdin.readline())
for i in range(num):
    count = 0
    n, m = map(int, sys.stdin.readline().split())
    queue_idx = deque(list(range(n)))
    imp = deque(sys.stdin.readline().split())

    while imp:
        if imp[0]==  max(imp):
            count += 1
            imp.popleft()
            if queue_idx.popleft() == m:
                print(count)

        else:
           
            imp.append(imp.popleft())
            queue_idx.append(queue_idx.popleft())
