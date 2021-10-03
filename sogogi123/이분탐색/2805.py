import  sys
n, m = map(int,sys.stdin.readline().split())
h= list(map(int,sys.stdin.readline().split()))

def searchbinary(left, right):
    while left <= right:
        cnt = 0
        middle = (left+right)//2
        for i in range(n):
            if h[i]>=middle:
                cnt+=(h[i]-middle) #% 사용시 zero division error가 뜬다
        if cnt>=m:
            left = middle+1
        else:
            right = middle-1
    return right
print(searchbinary(1,max(h))) # 1이 아니고 최소값을 1 대신 넣었을 때 틀렸다고 출력되며 pypy3를 이용하지 않으면 시간초과가 발생한다