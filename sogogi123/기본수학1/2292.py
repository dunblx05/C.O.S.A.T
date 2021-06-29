num = int(input())

# count = 0
# stage =[1,7,19,37,61,70]
# for i  in range(len(stage)-1):
#     if stage[i] == 1:
#         count = 1
#     if stage[i]<num<=stage[i+1]:
#         count = i+2
# print(count)

count =1
bee = 1
while num >bee:
    bee += count*6
    count +=1
print(count)