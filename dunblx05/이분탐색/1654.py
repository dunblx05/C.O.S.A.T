import sys

k, n = map(int, sys.stdin.readline().split())
lan = []

for i in range(k):
    lan.append(int(sys.stdin.readline()))

def binary_search(low, high, data):
    global n
    while low <= high:
        line = 0
        mid = (low + high) // 2
        for i in data:
            line += i // mid

        if line >= n:
            low = mid + 1
        else:
            high = mid - 1
    return high

print(binary_search(1, max(lan), lan))