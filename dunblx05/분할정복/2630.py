import sys

n = int(sys.stdin.readline())
paper = []
white = 0
blue = 0
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

def cut(x, y, n):
    global white, blue
    cur = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if cur != paper[i][j]:
                cut(x, y , n//2)
                cut(x + n//2, y , n//2)
                cut(x, y + n//2, n//2)
                cut(x + n//2, y + n//2, n//2)
                return
                
    if cur == 0:
        white += 1
    else:
        blue += 1

cut(0,0,n)

print(white)
print(blue)