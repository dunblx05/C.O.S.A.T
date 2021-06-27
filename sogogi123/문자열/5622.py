string = list(input())
stringLenth = int(len(string))
timeList =[]
for i  in range(stringLenth):
    time = (ord(string[i])%65)//3+3
    if string[i] == "S":
        time =8
    elif string[i] =="Z":
        time =10
    elif string[i] =="Y":
        time =10
    elif string[i] =="V":
        time = 9

    timeList.append(time)
print(timeList)
print(sum(timeList))

