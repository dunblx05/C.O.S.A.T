num = int(input())
stage = 0

n =0
upper = 0
down = 0

while num>n:
    stage += 1
    n+=stage
gap = n-num
if stage%2==0:
    upper = stage-gap
    down = gap +1
else:
    upper =gap +1
    down = stage-gap
print("{0}/{1}".format(upper,down))    

    
