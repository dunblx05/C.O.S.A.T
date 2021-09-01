import sys
n = int(sys.stdin.readline())
arr = []
blue = 0
white = 0
for i in range(n):
    row= list(map(int, sys.stdin.readline().split()))
    arr.append(row)

def loop(x,y,n):
    global arr, blue, white
    chek = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if chek!= arr[i][j]:
                loop(x,y,n//2)
                loop(x+n//2,y,n//2)
                loop(x,y+n//2,n//2)
                loop(x+n//2,y+n//2,n//2)
                return
    if chek ==0:
        white +=1
    elif chek ==1:
        blue +=1
        return
loop(0,0,n)
print(white)
print(blue)