import sys
from collections import deque

n = int(sys.stdin.readline())
board = [[0 for _ in range(n)] for _ in range(n)]
k = int(sys.stdin.readline())

for _ in range(k):
    i, j = map(int, sys.stdin.readline().split())
    board[i-1][j-1] = 1

change = {}
l = int(sys.stdin.readline())

for _ in range(l):
    x, c = sys.stdin.readline().split()
    change[int(x)] = c

snake = deque([[0, 0]])

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 벽에 부딪히는지 확인하는 함수
def check(x, y):
    if 0 <= x and x < n and 0 <= y and y <n:
        return True
    else:
        return False

# 현재 방향
cur_dir = 1
time = 0
cur_x, cur_y = 0, 0

def change_dir(d, c):
    # 오른쪽으로 회전, 1 -> 2 -> 3 -> 0 -> 1
    if c == 'D':
        d = (d + 1) % 4
    # 왼쪽으로 회전, 1 -> 0 -> 3 -> 2 -> 1    
    else:
        d = (d - 1) % 4
    return d

while True:
    time += 1
    cur_x += dx[cur_dir]
    cur_y += dy[cur_dir]

    if time in change.keys():
        cur_dir = change_dir(cur_dir, change[time])
    if check(cur_x, cur_y):
        # 뱀이 자기 몸에 부딪힌 경우
        if [cur_x, cur_y] in snake:
            break
        
        # 다음 위치에 사과가 있는 경우
        if board[cur_x][cur_y] == 1:
            board[cur_x][cur_y] = 0
            snake.append([cur_x, cur_y])
        
        # 다음 위치에 사과가 없는 경우
        elif board[cur_x][cur_y] == 0:
            snake.append([cur_x, cur_y])
            snake.popleft()
    else:
        break



print(time)