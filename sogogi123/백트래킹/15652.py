import itertools
num,col =map (int, input().split())
numList = []


for i in range(1,num+1):
    numList.append(i)
Lists =list(itertools.combinations_with_replacement(numList,col))

for i in Lists:
    for j in range(col):
        print(i[j],end = " ")
    print()