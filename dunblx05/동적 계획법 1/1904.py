import sys

n = int(sys.stdin.readline())

bin_list = [1, 2]

for i in range(2,n):
    bin_list.append((bin_list[i-2] + bin_list[i-1]) % 15746)

print(bin_list[n-1])

# 1 1
# 2 2
# 3 3
# 4 5
# 5 8