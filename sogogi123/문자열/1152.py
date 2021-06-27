string = input().split(" ")
if string[0] =="":
    del(string[0])
if string[len(string)-1] =="":
    del(string[len(string)-1])
print(len(string))


# string = input()
# count = 0
# pre = ""
# for i in string:
#     if string[0]== " ":
#         pass   
#     elif i ==" ":
#         count += 1
    
# print(count)
