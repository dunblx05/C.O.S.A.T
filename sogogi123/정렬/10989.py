# 카운터 정렬
import  sys
num  = int(sys.stdin.readline())

count = [0]* 10001
for i in range(num):
    count[(int(sys.stdin.readline()))] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)

# # 카운터 정렬 기본 형태
# import  sys
# num  = int(sys.stdin.readline())
# numList = []
# count = [0]* max(numList)+1
# for i in range(num):
#     numList.append(int(sys.stdin.readline()))

# for i in range(num):
#     count[numList[i]] +=1
# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i)