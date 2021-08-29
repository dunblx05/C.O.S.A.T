import sys

n = int(sys.stdin.readline())
stack = []
op = []
count = 1
valid = True

for i in range(n):
    num = int(sys.stdin.readline())

    while count <= num:
        stack.append(count)
        op.append("+")
        count += 1

    if stack[-1] == num:
        stack.pop()
        op.append("-")
    else:
        valid = False

if valid == False:
    print("NO")
else:
    for sig in op:
        print(sig)