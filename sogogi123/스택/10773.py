import sys
num = int(sys.stdin.readline())
stack = []
for i in range(num):
    n = int(sys.stdin.readline())
    if n ==0:
        stack.pop()
    else:
        stack.append(n)
    
print(sum(stack))