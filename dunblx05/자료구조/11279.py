import sys
import heapq

heap = []
n = int(sys.stdin.readline())

for _ in range(n):
    command = int(sys.stdin.readline())
    if command == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, [-command, command])