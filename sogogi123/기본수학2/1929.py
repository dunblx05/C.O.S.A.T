def Findss(n):
    if n== 1:
        return False
    if n ==2:
        return True
    for i in range(2,int(n **0.5)+1):
        if n%i ==0:
            return False
    return True

m,n = map(int,input().split())

# def ssfind(n):
#     global m
#     numlist= []
#     numlist = [True] *n
#     small = int(n**0.5)
#     for i in range(2,small+1):
#         if Findss(i):
#             for j in range(i+i,n,i):
#                 numlist[j-m] =False
       
#         return [i for i in range(m,n) if numlist ==True]
for i in range(m,n+1):
    if Findss(i):  
        print(i)
