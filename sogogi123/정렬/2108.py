import  math
import collections
import sys

num = int(sys.stdin.readline())
numList= []

for i  in range(num):
    numList.append(int(sys.stdin.readline()))
numList.sort()
count = []
count = collections.Counter(numList).most_common()


print(round((sum(numList))/len(numList)))

print(numList[len(numList)//2])

if len(count)>1:
    if count[0][1]==count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(numList[0])

if len(numList)>1:   
    print(numList[-1]-numList[0])
else:
    print(0)