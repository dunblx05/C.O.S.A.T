import sys
from collections import deque
num = int(sys.stdin.readline())
n=list(map(int, sys.stdin.readline().split()))

stack = deque()
res =[-1]*num

for i in range(num):
    while stack and (stack[-1][0]<n[i]):
        
        tmp,idx = stack.pop()
        res[idx] =n[i]
    stack.append([n[i],i])
        
print(*res)

#풀이 참고 사이트
#https://hooongs.tistory.com/329


###########################################################
# 시간초과
# for i in range(num):
#     stack =[]
#     for j in range(i,num):
#         if n[i]<n[j]:
#             stack.append(n[j])
            

#     if not stack:
#         print(-1, end= " ")
#     else:
#         print(stack[0],end=" ")