# 0 1
# ----
# 1 0	0
# 0 1	1
# 1 1	2
# 1 2	3
# 2 3	4
# 3 5	5

import sys

t = int(sys.stdin.readline())

zero_list = [1, 0]
one_list = [0, 1, 1]

for i in range(2,41):
    zero_list.append(zero_list[i-1] + zero_list[i-2])

for i in range(3, 41):
    one_list.append(one_list[i-1] + one_list[i - 2])

for i in range(t):
    a = int(sys.stdin.readline())
    print(zero_list[a], one_list[a])