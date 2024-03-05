# 11724 연결 요소의 개수

import sys
sys.setrecursionlimit(100000)
def dfs(v):
    visited[v] = 1
    graph[v].sort()
    for node in graph[v]:
        if visited[node] == 0:
            dfs(node)

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)] # 각 정점마다 연결되어 있는 그래프 표시

for item in arr: # 단방향이라는 얘기가 없으니 양방향으로 만들어준다.
    graph[item[0]].append(item[1])
    graph[item[1]].append(item[0])

visited = [0]*(N+1) # 방문배열
cnt = 0 # 서로 연결된 요소의 개수를 확인하기위한 용도
for item in graph:
    for node in item:
        if visited[node] == 0:
            dfs(node)
            cnt += 1
            
for i in range(1,len(visited)): # 만약 visited로 처리되자않은 경우
    if visited[i] == 0:         # 즉 간선이 연결되어있지 않은 경우
        cnt += 1                # 정점만 덩그러니 있는 경우에는 정점당 개수를 추가해줘야함
print(cnt)