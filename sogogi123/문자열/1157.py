num = []
A = input().upper()
AsetList = list(set(A))

for _ in AsetList:
    ACount = A.count(_)
    num.append(ACount)

if num.count(max(num))>=2:
    print("?")
else:
    print(AsetList[num.index(max(num))].upper())
            

