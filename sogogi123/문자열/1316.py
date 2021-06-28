num = int(input())
count = 0
for i in range(num):
    string = input()
    for r in range(len(string)):
        if r != len(string)-1:
            if string[r] == string[r+1]:
                pass
            elif string[r] in string[r+1:]:
                break
        else:
            count+=1
print(count)
