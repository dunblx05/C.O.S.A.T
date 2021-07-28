import sys
from functools import cache

@cache # 캐쉬 메모리를 사용하면 재귀 함수를 이용해서도 풀이가능
def p(n):
    if n <4:
        return 1
    else:
        return p(n-2)+ p(n-3)
num = int(sys.stdin.readline())
for i in range(num):
    a = int(sys.stdin.readline())
    print(p(a))


