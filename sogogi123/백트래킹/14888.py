import sys
def cul(i,res,a,s,m,d): 
    global maxi ,mini
    if i==num:
        maxi = max(res, maxi)
        mini = min(res, mini)
        
    else:
        if a:
            cul(i+1,res+numList[i],a-1,s,m,d) # 더하기
        if s:
            cul(i+1,res-numList[i],a,s-1,m,d) # 빼기
        if m:
            cul(i+1,res*numList[i],a,s,m-1,d)# 곱하기
        if d:
            cul(i+1,int(res/numList[i]),a,s,m,d-1)#나누기 여기서 //를 써버리면 수가 작게 나와버림
        
num = int(sys.stdin.readline())
numList =list(map(int, input().split()))
a,s,m,d = map(int,input().split())
maxi, mini = -1e9,1e9 #최대 정수값을 나타내는 방법이다
cul(1,numList[0],a,s,m,d)
print(maxi)
print(mini)

