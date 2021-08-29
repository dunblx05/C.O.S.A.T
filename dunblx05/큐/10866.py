import sys
from collections import deque

n = int(sys.stdin.readline())
deck = deque([])

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        deck.appendleft(int(command[1]))
    
    elif command[0] == 'push_back':
        deck.append(int(command[1]))

    elif command[0] == 'pop_front':
        if not deck:
            print(-1)
        else:
            print(deck.popleft())
    
    elif command[0] == 'pop_back':
        if not deck:
            print(-1)
        else:
            print(deck.pop())
    
    elif command[0] == 'size':
        print(len(deck))
    
    elif command[0] == 'empty':
        if not deck:
            print(1)
        else:
            print(0)
    
    elif command[0] == 'front':
        if not deck:
            print(-1)
        else:
            print(deck[0])

    elif command[0] == 'back':
        if not deck:
            print(-1)
        else:
            print(deck[-1])