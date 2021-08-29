import sys

while 1:
    is_empty = False
    string = sys.stdin.readline().rstrip()
    stack = []
    
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                is_empty = True
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                is_empty = True
                break
    if string == '.':
        break
    print("yes" if is_empty == False and len(stack) == 0 else "no")