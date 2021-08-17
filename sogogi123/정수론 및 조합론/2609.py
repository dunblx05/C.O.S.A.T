#################################
#런타임에러
# import sys
# a, b =map(int,sys.stdin.readline().split())

# def factor(n):
#     factor_list =[]
#     for i in range(2,n+1):
#         if n%i ==0:
#             factor_list.append(i)
#     return factor_list
# a_factor = set(factor(a))
# b_factor = set(factor(b))
# mixed_factor =a_factor & b_factor
# print(max(mixed_factor))
# print((a//max(mixed_factor))*(b//max(mixed_factor))*max(mixed_factor))

#######################################
# 두번째 방법 유클리드 호제법을 이용하자
import sys 
A, B = map(int, sys.stdin.readline().split()) 
a, b = A, B 
while b != 0: 
    a = a % b 
    a, b = b, a    
# gcd 
print(a) 
#lcm 
print(A*B//a)
