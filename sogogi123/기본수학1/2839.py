num = int(input())
bag = 0
while num >=0:
    if num %5 ==0:
        bag += num//5
        print(bag)
        break
    num -= 3
    bag+=1

else:
    print(-1)
        