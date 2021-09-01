import sys
n =list(map(int,sys.stdin.readline().split()))
def multiply(a,b):
    global n
    if b ==1:
        return a%n[2]
    
    temp = (multiply(a,b//2))
    if b%2 == 0:
        return temp *temp%n[2]
        
    else:
        return temp *temp* a %n[2]
    

print(multiply(n[0],n[1]))