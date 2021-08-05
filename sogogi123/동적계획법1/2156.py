import sys
num = int(sys.stdin.readline())

wine = [0 for _ in range(num+1)]
drinked = [0]

for i in range(1,num+1):
    wine[i] = int(input())

drinked.append (wine[1])
if num>1:
    drinked.append(wine[1] + wine[2])

for i in range(3,num+1):
    drinked[i].append(max(drinked[i-2]+ wine[i],drinked[i-3]+wine[i-1]+wine[i],drinked[i-1]))

print(drinked[num])