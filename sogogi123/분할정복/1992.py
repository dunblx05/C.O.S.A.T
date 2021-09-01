import sys
n = int(sys.stdin.readline())
arr = []
blue = 0
white = 0
for i in range(n):
    row= list(map(int, sys.stdin.readline().strip()))
    arr.append(row)

def loop(x,y,n):
    global arr
    if (n==1):
        return str(arr[x][y])
    
    res = []
    chek = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if chek!= arr[i][j]:
                res.append('(')
                res.extend(loop(x,y,n//2))
                res.extend(loop(x,y+n//2,n//2))
                res.extend(loop(x+n//2,y,n//2))       
                res.extend(loop(x+n//2,y+n//2,n//2))
                res.append(')')
                return res
    return str(chek)
    
print(''.join(loop(0,0,n)))
