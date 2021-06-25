num = int(input())
score=list((map(int,input().split())))
sumScore= []
for i in range(num):

    M = max(score)
    sumScore.append(score[i]/M*100)
print(sum(sumScore)/num)
