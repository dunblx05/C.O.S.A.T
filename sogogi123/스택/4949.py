import sys
while True:
    string = sys.stdin.readline().rstrip()
    if string == ".":
        break
    res = True
    stack = []
    for i in string:
        if i =="(" or i=="[":
            stack.append(i)
        elif i==")":
            if not stack or stack[-1]=="[":
                res = False
                break
            elif stack[-1] =="(":
                stack.pop()
        elif i=="]":
            if not stack or stack[-1]=="(": #not list 의 형태는 list 안이 비었는지 확인해 준다 not list =True 라면 비었다는 뜻
                res = False
                break
            elif stack[-1] =="[":
                stack.pop()
    if res ==True and not stack:
        print("yes")
    else:
        print("no")    
