import sys

t = int(sys.stdin.readline())

for i in range(t):
    sticker = []
    n = int(sys.stdin.readline())

    for j in range(2):
        sticker.append(list(map(int,input().split())))

    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
    else:
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]

        for k in range(2, n):
            # 현재 열까지 스티커를 선택한 값은 왼쪽 대각선의 값 혹은 그 값의 왼쪽 값
            sticker[0][k] += max(sticker[1][k - 1], sticker[1][k - 2])
            # 현재 열까지 스티커를 선택한 값은 왼쪽 대각선의 값 혹은 그 값의 왼쪽 값
            sticker[1][k] += max(sticker[0][k - 1], sticker[0][k - 2])
        print(max(sticker[0][n - 1], sticker[1][n - 1]))