import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

def binary_search(low, high, tree):
    global m
    while low <= high:
        tree_get = 0
        mid = (low + high) // 2

        for i in tree:
            if i - mid >= 0:
                tree_get += i - mid
            else:
                tree_get += 0
        
        if tree_get >= m:
            low = mid + 1
        else:
            high = mid - 1
    
    return high

print(binary_search(1, max(tree), tree))