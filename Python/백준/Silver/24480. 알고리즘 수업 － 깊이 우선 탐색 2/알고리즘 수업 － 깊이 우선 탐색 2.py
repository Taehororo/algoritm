# 24480. 알고리즘 수업 - 깊이 우선 탐색2

def dfs(v):
    global cnt
    visited[v] = cnt
    cnt += 1
    graph[v].sort(reverse=True) # 24479에서 reverse=True 만 추가
    for node in graph[v]:
        if visited[node] == 0:
            dfs(node)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split()) # 정점의 수 N, 간선의 수 M 시작정점 R
graph = [[] for _ in range(N+1)] # 인덱스번호가 곧 정점 각 data에는 연결된 정점의 인덱스가 주어진다.
visited = [0]*(N+1)

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 1 # 몇번째로 방문해는지 적기위한용도
dfs(R)

for i in range(1,N+1):
    print(visited[i])