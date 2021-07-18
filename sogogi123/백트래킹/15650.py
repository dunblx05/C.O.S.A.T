# import itertools
# num,col =map (int, input().split())
# numList = []


# for i in range(1,num+1):
#     numList.append(i)
# Lists =list(itertools.combinations(numList,col))

# for i in Lists:
#     for j in range(col):
#         print(i[j],end = " ")
#     print()

# n , m = map (int, input().split())
# numList =[]
# def per(start):
#     if len(numList) == m:
#         print(" ".join(map(str,numList)))
#         return
    
#     for i in range(start,n+1):
#         if i in numList:
#             continue
#         numList.append(i)
#         per(i+1)
#         numList.pop()
# per(1)

for i in range(10):
    if i % 2 == 0:
        continue
        print(i)    
    print(i)
print("Done")