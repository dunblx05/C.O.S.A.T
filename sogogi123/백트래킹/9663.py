num = int(input())
row = [0]*num
count = 0
def isZero(x):
    for i  in range(x):
        if row[x] == row[i] or abs(row[x]-row[i])== x-i:
            return 0
    return 1
def dfs(n):
    global count
    if n == num:
        count+=1
    else:
        for i in range(num):
            row[n] =i
            if isZero(n):
                dfs(n+1)

dfs(0)
print(count)

# n = int(input())
# s = [0 for i in range(16)]
# result = 0
# def isTrue(x):
#     for i in range(1, x):
#         if s[x] == s[i] or abs(s[x] - s[i]) == x - i:
#             return False
#     return True
# def dfs(cnt):
#     global result
#     if cnt > n:
#         result += 1
#     else:
#         for i in range(1, n + 1):
#             s[cnt] = i
#             if isTrue(cnt):
#                 dfs(cnt + 1)
# dfs(1)
# print(result)