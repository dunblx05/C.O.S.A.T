
start= int(input())
def sum_cycle(start):
    global count
    count = 0
    node = start
    
    while True:
        nextp = ((node-(node%10))//10)+ (node%10)
        nextp = (node%10)*10 +nextp%10
        node = nextp
        count +=1
        if nextp == start:
            break

sum_cycle(start)
print(count)



