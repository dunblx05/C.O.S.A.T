# 예제 입력
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

# 예제 출력
# 45

import sys

n = int(sys.stdin.readline())

day = []
profit = []
dp = [0 for _ in range(n + 1)]

for i in range(n):
    t, p = map(int,input().split())
    day.append(t)
    profit.append(p)

for i in range(n - 1, -1, -1):
    # 상담에 걸리는 시간과 현재 일수를 더한 값이 전체 일수를 넘어가면
    if day[i] + i > n:     
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], profit[i] + dp[i + day[i]])

print(dp[0])