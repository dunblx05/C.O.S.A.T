import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, n + 1)])
yos = []
while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())
    yos.append(queue.popleft())

print("<", end = "")
for i in range(n - 1):
    print(str(yos[i]) + ",", end = " ")

print(str(yos[-1]) + ">")