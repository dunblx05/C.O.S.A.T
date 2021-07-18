# import itertools
# num,col =map (int, input().split())
# numList = []


# for i in range(1,num+1):
#     numList.append(i)
# Lists =list(itertools.permutations(numList,col))

# for i in Lists:
#     for j in range(col):
#         print(i[j],end = " ")
#     print()


n , m = map (int, input().split())
numList =[]
def per():
    if len(numList) == m:
        print(" ".join(map(str,numList)))
        return
    
    for i in range(1,n+1):
        if i in numList:
            continue
        numList.append(i)
        per()
        numList.pop()
per()