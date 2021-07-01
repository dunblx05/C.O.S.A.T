Test_case =int(input())
for _ in range(Test_case):
    k =int(input())
    n = int(input())
    floor = list(range(1,15))
    for i in range(0,k):
        for j in range(1,n+1):
            floor[j] += sum(floor[j-1:j])
    print(floor[n])