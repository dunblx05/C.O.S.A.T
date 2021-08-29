import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        push_num = int(command[1])
        stack.append(push_num)
    elif command[0] == 'pop':
        if not stack:
            print("-1")
        else:
            pop_num = stack.pop()
            print(pop_num)
    elif command[0] == 'top':
        if not stack:
            print("-1")
        else:
            print(stack[-1])
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if not stack:
            print("1")
        else:
            print("0")