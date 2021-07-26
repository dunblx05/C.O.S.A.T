import sys

num = int(sys.stdin.readline())

stat = [list(map(int, input().split())) for n in range(num)]
visited =[False for a in range(num)]
ans = 1000

def cal_stat(i, cnt):
    global ans
    if cnt == num // 2:
        start , link = 0, 0

        for i in range(num):
            for j in range(num):
                if visited[i] and visited[j]:
                    start += stat[i][j]

                elif not visited[i] and not visited[j]:
                    link += stat[i][j]

        ans = min(ans, abs(start - link))
    
    for k in range(i, num):
        if visited[k]:
            continue
        visited[k] = True
        cal_stat(k + 1, cnt +1)
        visited[k] = False

cal_stat(0,0)
print(ans)