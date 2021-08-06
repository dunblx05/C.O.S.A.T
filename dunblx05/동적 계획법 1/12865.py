import sys

n, k = map(int,input().split())

# D.P 배열
profit = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

# 물건 배열
object = [[0 for _ in range(2)] for _ in range(n)]

for i in range(n):
    object[i] = list(map(int,(input().split())))


for i in range(1, n + 1):
    for j in range(1, k + 1):
            # i번째 물건의 무게가 현재 배낭의 무게 한도보다 무겁지 않다면
            if object[i-1][0] <= j:
                # i번째 물건만큼의 무게를 비운 최적값 + 현재 물건의 가치 or i -1개의 물건을 가지고 구한 전 단계의 최적값 중 큰 값
                profit[i][j] = max(profit[i-1][j], object[i-1][1] + profit[i-1][j-object[i-1][0]])
            # i번째 물건이 배낭의 무게보다 무겁다면
            else:       
                # i - 1개의 물건을 가지고 구한 가치의 최적값
                profit[i][j] = profit[i-1][j]

print(profit[n][k])