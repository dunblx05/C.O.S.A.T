import sys

n = int(sys.stdin.readline())
video = []

for _ in range(n):
    video.append(list(map(int, sys.stdin.readline().strip())))

def quad(x, y, n):
    cur = video[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if cur != video[i][j]:
                print("(", end = "")
                quad(x, y, n//2)
                quad(x, y + n//2, n//2)
                quad(x + n//2, y, n//2)
                quad(x + n//2, y + n//2, n//2)
                print(")", end = "")
                return
                
    if cur == 1:
        print("1", end = "")
        
    else:
        print("0", end = "")
        

quad(0,0,n)