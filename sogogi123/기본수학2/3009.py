xlist =[]
ylist=[]
for _ in range(3):
    
    x,y = map(int, input().split())

    xlist.append(x)
    ylist.append(y)
for i in range(3):
    if xlist.count(xlist[i])==1:
        sx=xlist[i]
    if ylist.count(ylist[i])==1:
        sy = ylist[i]

print(sx,sy)