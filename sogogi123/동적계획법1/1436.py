import sys
num = int(sys.stdin.readline())
count = [0 for _ in range(num+1)]

for i in range(2,num+1):
    count[i] = count[i-1]+1

    if i %2==0 and count[i]> count[i//2]+1:
        count[i] = count[i//2]+1
    if i %3==0 and count[i]> count[i//3]+1:
        count[i] = count[i//3]+1

print(count[num])