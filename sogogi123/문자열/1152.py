string = input().split(" ")
if string[0] =="":
    del(string[0])
if string[len(string)-1] =="":
    del(string[len(string)-1])
print(len(string))
