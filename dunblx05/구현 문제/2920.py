import sys

numlist = list(map(int, sys.stdin.readline().split()))

ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]

if numlist == ascending:
    print("ascending")
elif numlist == descending:
    print("descending")
else:
    print("mixed")