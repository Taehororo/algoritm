# 1260. DFS와 BFS
from collections import deque

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    graph[v].sort()
    for node in graph[v]:
        if visited[node] == 0:
            dfs(node)

def bfs(v):
    visited2[v] = 1
    queue = deque([v])
    while queue:
        node = queue.popleft()
        print(node, end =' ')
        graph[node].sort()
        for idx in graph[node]:
            if visited2[idx] == 0:
                visited2[idx] = 1
                queue.append(idx)


N, M, V = map(int, input().split())
visited = [False] * (N+1)
arr = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for i in range(N+1)]
for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
visited1 = [0]*(N+1)
visited2 = [0]*(N+1)

dfs(V)
print()
bfs(V)