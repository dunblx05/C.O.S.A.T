num = int(input())

numList = []
for i in range(num):
    numList.append(int(input()))
    numList.sort()
for j in numList:
    print(j)
