Test_case =int(input())
for _ in range(Test_case):
    k =int(input())
    n = int(input())
    beforefloor = list(range(1,15))
    for i in range(k):
        for j in range(1,n):
            beforefloor[j] += beforefloor[j-1]
    print(beforefloor[n-1])