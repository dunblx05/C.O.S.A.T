import sys

def cal(a, s, m, d, i, ans):
    global max_ans, min_ans
    if i == n:
        max_ans = max(ans, max_ans)
        min_ans = min(ans, min_ans)
    else:
        if a:
            cal(a - 1, s, m, d, i + 1, ans + numlist[i])
        if s:
            cal(a, s - 1, m, d, i + 1, ans - numlist[i])
        if m:
            cal(a, s, m - 1, d, i + 1, ans * numlist[i])
        if d:
            cal(a, s, m, d - 1, i + 1, int(ans / numlist[i]))

max_ans = -10E9
min_ans = 10E9

n = int(sys.stdin.readline())

numlist = list(map(int, input().split()))

add, sub, multiple, divide = map(int, input().split())

cal(add, sub, multiple, divide, 1, numlist[0])

print(max_ans)
print(min_ans)