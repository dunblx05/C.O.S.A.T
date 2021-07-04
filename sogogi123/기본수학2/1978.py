def Findss(n):
    if n== 1:
        return False
    if n ==2:
        return True
    for i in range(2,n):
        if n%i ==0:
            return False
    return True

count = 0
num = int(input())
numbers = list(map(int,input().split()))

for i in numbers:
    if Findss(i):
        count+=1
print(count)