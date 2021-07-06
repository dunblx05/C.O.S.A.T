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
for i in range(1,123456*2):
    if Findss(i):
        numList.append(i)
        
while True:
    num = int(input())
    count = 0
    if num == 0:
        break
    for j in numList:
        if num < j<= num*2:
            count +=1
    print (count)








# while True :
    
#     num = int(input())
    
#     numList =[]
#     M = 2*num
#     for i in range(num+1, M+1):
#         if Findss(i):
#             numList.append(i)
#     if num == 0:
#         break
#     print(len(numList))