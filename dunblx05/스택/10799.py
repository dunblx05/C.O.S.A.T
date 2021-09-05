import sys

laser = sys.stdin.readline().rstrip()
stack = []
bar = 0

for i in range(len(laser)):
    if laser[i] == '(':
        stack.append('(')
    else:
        if laser[i-1] == '(':
            stack.pop()
            bar += len(stack)
        else:
            stack.pop()
            bar += 1

print(bar)