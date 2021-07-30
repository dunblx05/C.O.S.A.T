import sys

n = int(sys.stdin.readline())

stair = [0 for i in range(0,301)]
score = [0 for i in range(0,301)]

for i in range(n):
    stair[i] = int(input())

score[0] = stair[0]
score[1] = stair[0] + stair[1]
score[2] = max(stair[1] + stair[2], stair[0] + stair[2])

for i in range (3,n):
    score[i] = max(score[i-3] + stair[i-1] + stair[i], score[i-2] + stair[i])

print(score[n-1])