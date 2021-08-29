import sys

n = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))
stack = []
res = [-1 for _ in range(n)]

stack.append(0)

# for문을 두번 사용하면 시간초과, stack을 index로 사용하여 for문 한번만 사용
for i in range(1, n):
    while len(stack) != 0 and numlist[stack[-1]] < numlist[i]:
        res[stack.pop()] = numlist[i]
    stack.append(i)

print(*res)