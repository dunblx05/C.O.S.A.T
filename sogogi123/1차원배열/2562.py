num =[]
for _ in range(9):
    num.append(int(input()))
num.sort()
print(num)
M = max(num)
I = num.index(M)+1
print(M)
print(I)