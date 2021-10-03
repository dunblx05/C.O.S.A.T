import sys

l = int(sys.stdin.readline().strip())
str = sys.stdin.readline().rstrip()
r = 31
m = 1234567891
res = 0
count = 0

for i in str:
    res += ((ord(i) - 96) * pow(r, count))
    count += 1

print(res % m)