import sys

n = int(sys.stdin.readline())
paper = []
minus = 0
zero = 0
plus = 0

for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

def cut(x, y, n):
    cur = paper[x][y]
    global minus, zero, plus

    for i in range(x, x + n):
        for j in range(y, y + n):
            if cur != paper[i][j]:
                cut(x, y, n//3)
                cut(x + n//3, y, n//3)
                cut(x + 2 * n//3, y, n//3)
                cut(x, y + n//3, n//3)
                cut(x + n//3, y + n//3, n//3)
                cut(x + 2 * n//3, y + n//3, n//3)
                cut(x, y + 2 * n//3, n//3)
                cut(x + n//3, y + 2 * n//3, n//3)
                cut(x + 2 * n//3, y + 2 * n//3, n//3)
                return

    if cur == -1:
        minus += 1
    elif cur == 0:
        zero += 1
    elif cur == 1:
        plus += 1

cut(0, 0, n)
print(minus, zero, plus, sep = "\n")