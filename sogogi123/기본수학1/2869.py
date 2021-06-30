import math
A,B,V = map(int,input().split())
day = A-B
date= (V-B)/(A-B)

print(math.ceil(date))


# while V>(day*date+A):
#     date+=1
# print(date+1)