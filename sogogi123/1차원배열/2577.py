A,B,C = [int(input()) for i in range(3)]
result_arr = []
result = A*B*C
result_arr = list(str(result))

for _ in range(10):
    print(result_arr.count(str(_)))
