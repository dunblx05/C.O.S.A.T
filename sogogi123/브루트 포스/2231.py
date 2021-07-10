num = int(input())

numList = []
result = []
for A in range(num):
    for i in str(A):
        numList.append(int(i))
    if num == A + sum(numList):
        result.append(A)
    numList =[]


if len(result) ==0:
    print(0)
else:
    print(min(result))