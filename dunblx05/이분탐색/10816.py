import sys
from collections import Counter

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

n = int(sys.stdin.readline())
num_card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
count_num = list(map(int, sys.stdin.readline().split()))

num_card.sort()
c = Counter(num_card)   #list의 원소 개수를 세어서 dict로 만듬
res = [0 for _ in range(m)]

for i in range(m):
    #이진 탐색으로 찾는 숫자가 있는지 확인
    index = binary_search(count_num[i], num_card)
    if index == -1:
        continue

    res[i] = c[count_num[i]]

for i in range(m):
    print(res[i], end = ' ')