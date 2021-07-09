num = int(input())
star = [["*"for i in range(num)]for j in range(num)]

def d(n):
    global star
    col,row = 0,0
    count =0
    if n ==3:
        for col in range(num):
            for row in range(num):
                if col % 3 == 1 and row %3 ==1:
                    star[col][row] = " "
    if n>=9:
        d(n//3)
        for col in range(num):
            for row in range(num):
                if col//(n//3) in range(1,num,3) and row//(n//3) in range(1,num,3):
                    star[col][row] = " "
                
d(num)

for i in range(num):
    for j in range(num):
        print(star[i][j],end = "")
    print()




# def concatenate(r1, r2):
#     return [''.join(x) for x in zip(r1, r2, r1)]
 
# def star10(n):
#     if n == 1:
#         return ['*']
#     n //= 3
#     x = star10(n)
#     a = concatenate(x, x)
#     b = concatenate(x, [' '*n]*n)
 
#     return a + b + a
 
# print('\n'.join(star10(int(input()))))