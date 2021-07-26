# import  sys

# def fibo(n):
#     global zero_count, one_count
#     if n==0:
#         zero_count +=1
#         return 0       
#     elif n ==1:
#         one_count +=1
#         return 1        
#     else:
#         return fibo(n-1)+ fibo(n-2)

# num = int(sys.stdin.readline())
# for i in range(num):
#     count = 0
#     zero_count = 0
#     one_count =0
#     a= int(sys.stdin.readline())
#     fibo(a)
#     print(zero_count, one_count)

#####
#  규칙
# n	    0	1	2	3	4	5
# zero	1	0	1	1	2	3
# one	0	1	1	2	3	5

num = int(input())
for i in range(num):
    n = int(input())
    zero =1
    one = 0
    temp = 0
    for j in range(n):
        temp = one
        one = one + zero
        zero = temp
    print(zero, one)