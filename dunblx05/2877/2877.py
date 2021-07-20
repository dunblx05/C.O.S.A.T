import sys

k = int(sys.stdin.readline())

binary = format(bin(k + 1)[3:])

for i in binary:
    if i == '0':
        print(4,end="")
    elif i == '1':
        print(7,end="") 