num_list =[]
for _ in range(9):
    num_list.append(int(input()))

M = max(num_list)
I = num_list.index(M)+1
print(M)
print(I)