import  sys
k,n = map(int,sys.stdin.readline().split())

length = []

for _ in range(k):
    length.append(int(sys.stdin.readline()))
    length.sort(reverse=True)
def findbinary(left, right):
    
    while left<=right:
        cnt = 0
        middle = (left + right)//2

        for i in range(k):
            cnt+= (length[i]//middle)
        if cnt>=n:

            left =middle+1
        else:
            right = middle-1
    return print(right)


findbinary(1,length[0])