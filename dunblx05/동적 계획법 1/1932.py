#     0
#    0 1
#   0 1 2
#  0 1 2 3
# 0 1 2 3 4 

import sys

tri = []

n = int(sys.stdin.readline())

for i in range(n):
    tri.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(0,len(tri[i])):
        if j == 0:
            tri[i][j] = tri[i][j] + tri[i-1][j]
        elif j == len(tri[i]) - 1:
            tri[i][j] = tri[i][j] + tri[i-1][j-1]
        else:
            tri[i][j] = max(tri[i-1][j-1],tri[i-1][j]) + tri[i][j]

print(max(tri[n-1]))