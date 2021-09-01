import sys
n = int(sys.stdin.readline())
arr = []
zero = 0
one = 0
mione =0
for i in range(n):
    row= list(map(int, sys.stdin.readline().strip().split()))
    arr.append(row)

def loop(x,y,n):
    global arr ,zero, one, mione
    # if (n==1):
    #     return str(arr[x][y])
    
    
    chek = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if chek!= arr[i][j]:
            
                loop(x,y,n//3)
                loop(x,y+n//3,n//3)
                loop(x+n//3,y,n//3)   
                loop(x+n//3,y+n//3,n//3)
                loop(x+(n//3)*2,y,n//3)
                loop(x+(n//3)*2,y+n//3,n//3)
                loop(x,y+(n//3)*2,n//3)
                loop(x+n//3,y+(n//3)*2,n//3)
                loop(x+(n//3)*2,y+(n//3)*2,n//3)
                return 
    if chek ==0:
        zero +=1
    elif chek ==1:
        one +=1
    elif chek ==-1:
        mione +=1
    return

loop(0,0,n)
print(mione)
print(zero)
print(one)
