num, M = map(int, input().split())
numbers = list(map(int, input().split()))

sumList = []



for i in range (num):
    for j in range(i+1,num):
        for ij in range(j+1,num):
            if M>=numbers[i]+numbers[j]+numbers[ij]:
                sumList.append(numbers[i]+numbers[j]+numbers[ij])
print(max(sumList))

    



