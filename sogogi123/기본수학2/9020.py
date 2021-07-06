def Findss(n):
    if n== 1:
        return False
    if n ==2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
    return True

numList = []
for i in range(1,10000+1):
    if Findss(i):
        numList.append(i)

jList = []
nums = int(input())
for _ in range(nums):
    num = int(input())
    jList =[]
    for j in numList:
        if j< num:
            jList.append(j)


    half = num//2
    for m in range(half,1,-1):
        if (num - m in jList) and (m in jList):
            print(m,num-m)
            break
        

