row = int(input())
col =[]
count = 0
countSum=[]
for _ in range(row):
    col.append(input()) 
    for i in range(len(col[_])):
        if col[_][i] =="O":
            count +=1
            countSum.append(count)
        elif col[_][i] =="X":
            count =0
            countSum.append(count)

    print(sum(countSum))
    countSum = []
    count = 0    
    