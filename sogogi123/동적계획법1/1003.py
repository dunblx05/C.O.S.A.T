import  sys

def fibo(n):
    global zero_count, one_count
    if n==0:
        zero_count +=1
        return 0       
    elif n ==1:
        one_count +=1
        return 1        
    else:
        return fibo(n-1)+ fibo(n-2)

num = int(sys.stdin.readline())
for i in range(num):
    count = 0
    zero_count = 0
    one_count =0
    a= int(sys.stdin.readline())
    fibo(a)
    print(zero_count, one_count)

