import sys
from collections import deque

test = int(sys.stdin.readline())

for t in range(test):
    print_flag = True
    reverse_flag = False
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    numlist = sys.stdin.readline()[1:-2].split(",")
    
    if numlist[0] != '':
        numlist = deque(numlist)
    else:
        numlist = deque()

    for i in range(len(p)):
        if p[i] == 'R' and reverse_flag == False:
            reverse_flag = True
        elif p[i] == 'R' and reverse_flag == True:
            reverse_flag = False
        elif p[i] == 'D':
            if not numlist:
                print("error")
                print_flag = False
                break
            else:
                if reverse_flag == True:
                    numlist.pop()
                else:
                    numlist.popleft()
    
    if print_flag == True:
        if numlist and reverse_flag == False:
            print("[", end = '')
            for i in range(len(numlist) - 1):
                print(int(numlist[i]), end = ',')
            print(numlist[-1], end = '')
            print("]")
        elif numlist and reverse_flag == True:
            print("[", end = '')
            for i in range(len(numlist) - 1 , 0, -1):
                print(int(numlist[i]), end = ',')
            print(numlist[0], end = '')
            print("]")
        else:
            print("[]")