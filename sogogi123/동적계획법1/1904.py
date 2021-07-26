# 증가량이 피보나치 수열을 따른다
import sys
num = int(sys.stdin.readline())
arr =[0]*1000001
arr [1] = 1
arr[2] =2
for i in range(3,num+1):
    arr[i] =  (arr[i-1] + arr[i-2])%15746


print(arr[num])