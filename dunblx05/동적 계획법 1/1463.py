import sys

n = int(sys.stdin.readline())

# 연산횟수 리스트, cal[n]값은 n을 1로 만드는 최소 연산의 횟수
# 0, 1, 2, 3
cal = [0, 0, 1, 1]

for i in range(4, n + 1):       # n번째까지 반복해야 cal[n] 출력 가능
    cal.append(cal[i - 1] + 1)

    if i % 2 == 0:
        #append 사용하면 리스트 크기가 늘어나기 때문에 인덱싱으로 값 넣어줘야 함
        cal[i] = min(cal[i], cal[i//2] + 1)

    if i % 3 == 0:
        #append 사용하면 리스트 크기가 늘어나기 때문에 인덱싱으로 값 넣어줘야 함
        cal[i] = min(cal[i], cal[i//3] + 1)

# n을 1로 만드는 최소 연산의 횟수이기 때문에  cal[n - 1]이 아닌 cal[n]을 출력
print(cal[n])