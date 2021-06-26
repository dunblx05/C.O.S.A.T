inpNum = int(input())
num = []


for n in range(1, inpNum+1):
    if n <100:
        num.append(n)
    else:
        num1 = n%10
        num10 = (n%100 - num1)//10
        num100 = (n-num1-num10)//100
        if num1-num10 == num10-num100:
            num.append(n)

print(len(num))
        
        



