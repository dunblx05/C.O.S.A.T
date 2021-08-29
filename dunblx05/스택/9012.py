import sys

t = int(sys.stdin.readline())

for i in range(t):
    is_empty = False
    paren = list(sys.stdin.readline())
    valid = []
    for j in range(len(paren)):
        if paren[j] == '(':
            valid.append(1)
        elif paren[j] == ')':
            if len(valid) == 0:
                is_empty = True
            else:
                valid.pop()
    if len(valid) == 0 and is_empty == False:
        print("YES")
    else:
        print("NO")