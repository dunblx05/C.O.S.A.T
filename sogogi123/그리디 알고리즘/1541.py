a = input().split("-")
num_list = []
for i in a:
    sumnum = 0
    s = i.split("+")
    for j in s:
        sumnum+=int(j)
    num_list.append(sumnum)
n=num_list[0]
for i in range(1,len(num_list)):
    n-=num_list[i]
print(n)