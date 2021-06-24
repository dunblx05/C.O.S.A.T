import math

n = int(input())
for i  in range(n):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    rs = r1 + r2
    rm = abs(r1 - r2)
    if dist == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if dist == rs or dist == rm:
            print(1)
        elif dist < rs and dist > rm:
            print(2)
        else:
            print(0)