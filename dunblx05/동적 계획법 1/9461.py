# 1 1 1 2 2 3 4 5 7 9 12
# p(11) = p(6) + p(10)
# p(n) = p(n-5) + p(n-1)

import sys

tri = [1,1,1,2,2,3]

t = int(sys.stdin.readline())

for i in range(6, 101):
    tri.append(tri[i-5]+tri[i-1])

for i in range(t):
    n = int(sys.stdin.readline())
    print(tri[n-1])