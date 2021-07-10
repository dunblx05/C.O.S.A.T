num = int(input())
x,y =[], []

for _ in range(num):
    a, b =map (int, input().split())
    x.append(a)
    y.append(b)
for i in range(num):
    rank = 1
    for j in range(num):
        if x[i]<x[j]and y[i]<y[j]:
            rank+=1
    print(rank, end= "")
    