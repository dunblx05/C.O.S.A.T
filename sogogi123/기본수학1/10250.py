num = int(input())
for _ in range(num):
    H,W,N = map(int, input().split())

    if N%H !=0:
        print("{0}{1:0>2}".format(str(N%H),str(N//H+1)))
    

    else:
        print("{0}{1:0>2}".format(N,N//H))
