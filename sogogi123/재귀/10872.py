def d(n):
    if n<=0:
        return 1
    return n * d(n-1)


        
n =int(input())
print(d(n))