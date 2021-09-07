import sys
from collections import  Counter
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
# collection 모듈에서 Counter함수를 이용한 풀이
res  = Counter(n_list)
for i in m_list:
    if i in res:
        print(res[i],end = " ")
    else:
        print(0, end = " ")

########################################################
#해쉬 알고리즘을 이용한 풀이
# from sys import stdin
# _ = stdin.readline()
# N = map(int,stdin.readline().split())
# _ = stdin.readline()
# M = map(int,stdin.readline().split())
# hashmap = {}
# for n in N:
#     if n in hashmap:
#         hashmap[n] += 1
#     else:
#         hashmap[n] = 1
# for m in M:
#     if m in hashmap:
#         print(hashmap[m], end = " ")
#     else:
#         print(0, end = " ")



##########################################################
# 이진트리를 이용한 풀이 시간초과
# def binary(l,n_list,start,end):
#     global cnt
#     if start> end:
#         return 0
#     m = (start+end)//2
#     if l ==n_list[m]:
#        return n_list[start:end+1].count(l)
#     elif l<n_list[m]:
#         return binary(l,n_list,start,m-1)
#     else :
#         return binary(l,n_list,m+1,end)
    


# for l in m_list:
#     start = 0
#     end = len(n_list)-1
#     print(binary(l,n_list,start,end), end = " ")
