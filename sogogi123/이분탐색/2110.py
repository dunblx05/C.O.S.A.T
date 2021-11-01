import sys

N, C = map(int,sys.stdin.readline().split())
xi = []
for i in range(N):
    x = int(sys.stdin.readline().strip())
    xi.append(x)

xi.sort()

def binarysearch(array,start, end):
    while start<=end:
        mid = (start+end)//2
        cur = array[0]
        count =1

        for i in range(1,len(array)):
            if array[i]>=cur +mid:
                count+=1
                cur=array[i]
        if count >=C:
            global res
            start = mid +1
            res = mid
        else:
            end = mid -1
res = 0
start = 1
end = xi[-1] - xi[0]

binarysearch(xi,start,end)
print(res)