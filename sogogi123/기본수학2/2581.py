def Findss(n):
    if n== 1:
        return False
    if n ==2:
        return True
    for i in range(2,n):
        if n%i ==0:
            return False
    return True

m= int(input())
M = int(input())
numList = []
for i  in range(m, M+1):
    if Findss(i):
        numList.append(i)


if not numList:
    print(-1)
else:
    print(sum(numList))
    print(min(numList))

