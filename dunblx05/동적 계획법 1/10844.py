# 9 17 32 61 .....

# import sys

# n = int(sys.stdin.readline())

# stair_num = [9]

# for i in range(1, n + 1):
#     stair_num.append(stair_num[i-1] * 2 - i)

# print(stair_num[n-1]%1000000000)

# n의 자리수마다 끝에 올 수 있는 수의 갯수
#     0 1 2 3 4 5 6 7 8 9 
# 1   0 1 1 1 1 1 1 1 1 1 -> 9
# 2   1 1 2 2 2 2 2 2 2 1 -> 17
# 3   1 3 3 4 4 4 4 4 3 2 -> 32

import sys

n = int(sys.stdin.readline())

stair_num = [[0 for i in range(10)] for i in range(101)]

stair_num[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1, n):
    for j in range(0,10):
        if j == 0:
            stair_num[i][j] = stair_num[i-1][1]
        elif j == 9:
            stair_num[i][j] = stair_num[i-1][8]
        else:
            stair_num[i][j] = stair_num[i-1][j+1] + stair_num[i-1][j-1]

print(sum(stair_num[n-1]) % 1000000000)