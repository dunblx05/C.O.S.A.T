import sys
n = int(sys.stdin.readline())
count =0
stack = []
result = []
TorF = True
for i in range(n):
    x =int(sys.stdin.readline().rstrip())
    while count <x:
        count +=1
        stack.append(count)
        result.append("+")
    
    if stack[-1] ==x:
        stack.pop()
        result.append("-")
    else:
        TorF = False
        pass

if TorF == False:
    print("NO")
else:
    print("\n".join(result))
