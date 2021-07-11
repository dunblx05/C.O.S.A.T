# def qsort(arr, start, end):
#     if end<= start:
#         return
#     low = start
#     high = end
    
#     pivot = arr[(low + high)//2]
#     while low<=high:
#         while arr[low] <pivot:
#             low +=1
#         while arr[high] > pivot:
#             high -=1
#         if low <= high:
#             arr[low], arr[high]= arr[high], arr[low]
#             low,high = low +1 , high -1
#     mid =low
#     qsort(arr, start,mid-1)
#     qsort(arr,mid,end)

# def quicksort(ary):
#     qsort(ary,0,len(ary)-1)

# num = int(input())

# numList = []
# for i in range(num):
#     numList.append(input())

# quicksort(numList)
# for j in numList:
#     print(j)

num = int(input())

numList = []
for i in range(num):
    numList.append(int(input()))

numList = sorted(numList)
for j in numList:
    print(j)

