import sys
from collections import  deque
t = int(sys.stdin.readline())

for i in range(t):
    
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    xi = sys.stdin.readline()[1:-2].split(',')
    if xi[0] != '':
        xi = deque(xi)
    else:
        xi = deque()
    direction_flag = True
    if n==0:
        print('error')
        continue
    if len(xi)<p.count('D'):
            print('error')
            continue
    for j in range(len(p)):
        if p[j] == 'R':
            if direction_flag ==True:
                direction_flag =False
            elif direction_flag ==False:
                direction_flag = True

        elif p[j]  == 'D':
            if direction_flag ==True:
                xi.popleft()
            elif direction_flag ==False:
                xi.pop()
        
        if p.count('R') %2 !=0:
            xi.reverse()

    print("[",end="")
    for i in range(len(xi)):
        print(xi[i],end="")
        if i != len(xi)-1:
            print(",",end="")
    print("]")
        

















#################################
#시간 초과

# for i in range(t):
#     try:
#         p = sys.stdin.readline().strip()
#         n = int(sys.stdin.readline())
#         xi = deque(map(int,sys.stdin.readline()[1:-2].split(',')))

#         for j in range(len(p)):
            
          
#             if p[j] == 'R':
#                 xi.reverse()
#             elif p[j]  == 'D':
#                 xi.popleft()
#         print(list(xi))   
#     except:
#         print('error')
        
        
  

    