import sys

k = int(sys.stdin.readline())

money = []

for i in range(k):
    cost = int(sys.stdin.readline())
    if cost == 0:
        money.pop()
    else:
        money.append(cost)

if len(money) == 0:
    print(0)
else:
    print(sum(money))