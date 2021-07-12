import  sys
num = int(input())
humanList = []
for i in range(num):
    sorce = list((sys.stdin.readline().split()))
    sorce.append(i)
    humanList.append(sorce) 

humanList.sort(key=lambda human:(int(human[0]),int(human[2])))
for j in humanList:
    print(j[0],j[1])