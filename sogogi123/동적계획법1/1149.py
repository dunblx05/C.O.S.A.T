import sys
house = int(sys.stdin.readline())
arr = []
for i in range(house):
    arr.append(list(map(int,input().split())))
for i in range(1,house):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2])+ arr[i][0] # RGB 색을 칠하는 최소 값
    print(arr[i][0])
    arr[i][1] = min(arr[i-1][0], arr[i-1][2])+ arr[i][1]
    print(arr[i][1])
    arr[i][2] = min(arr[i-1][0], arr[i-1][1])+ arr[i][2]
    print(arr[i][2])
print(min(arr[house-1][0],arr[house-1][1],arr[house-1][2]))       
