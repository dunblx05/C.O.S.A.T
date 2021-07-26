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
