import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[0 for i in range(n + 1)] for i  in range(n + 1)]
visited1 = [0 for i in range(n + 1)]
visited2 = [0 for i in range(n + 1)]

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start][end] = graph[end][start] = 1

def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end = ' ')
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    q = deque()
    q.append(v)
    visited[v] = 1
    
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in range(1, n + 1):
            if visited[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited[i] = 1

dfs(graph, v, visited1)
print( )
bfs(graph, v, visited2)