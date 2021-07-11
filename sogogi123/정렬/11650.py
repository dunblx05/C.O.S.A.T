# num =int(input())
# xy = [[0 for _ in range(2)]for _ in range (num)]
# for i in range(num):
#     x,y = map(int, input().split())
#     xy[i][0] = x
#     xy [i][1]  = y
# xy = sorted(xy)
# for j in range(num):
#     print (xy[j][0],xy[j][1])

import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key=lambda x: (x[0], x[1]))
for i in so:
    print(i[0], i[1])
