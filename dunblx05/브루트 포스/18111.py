import sys

n, m, b = map(int, sys.stdin.readline().split())
ground = []
time, height = sys.maxsize, 0

for i in range(n):
    ground.append(list(map(int, sys.stdin.readline().split())))

# 0부터 256까지의 경우의 수 모두 해보기
for h in range(257):
    top = 0         #제거
    bottom = 0      #설치
    for i in range(n):
        for j in range(m):
            if ground[i][j] < h:
                bottom += (h - ground[i][j])
            else:
                top += (ground[i][j] - h)
    bag = top + b
    if bag < bottom:
        continue
    t = 2 * top + bottom
    if t <= time:
        time = t
        height = h

print(time, height)