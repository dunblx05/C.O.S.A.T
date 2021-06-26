N = int(input())
for _ in range(N):
    num,string = input().split()
    for i in range(len(string)):
        print(string[i]*int(num),end="")
    print()