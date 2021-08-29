import sys
from collections import deque

n = int(sys.stdin.readline())
deck = deque([i for i in range(1, n + 1)])
index = 1

while len(deck) != 1:
    if index % 2 == 1:
        deck.popleft()
    if index % 2 == 0:
        deck.append(deck.popleft())
    index += 1

print(deck[0])