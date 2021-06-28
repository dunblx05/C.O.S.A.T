string = input()
special =["c-","dz=", "d-","lj","nj","s=","z="]

for i  in special:
    string = string.replace(i, "a")
for _ in string:
    string = string.replace("=","")

print(len(string))    