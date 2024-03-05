import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(x):
    visited[x] = 1
    for node in graph[x]:
        if visited[node] == 0:
            dfs(node)
        else:
            parent[x] = node # 즉 이미 방문했을때 한마디로 끝에 도달했을때 연결된 애가 부모다
            

N = int(input())
arr = [list(map(int ,input().split())) for _ in range(N-1)]
graph = [[] for _ in range(N+1)]

for item in arr: # 방향에 대한 설명이 양방향으로 설정
    graph[item[0]].append(item[1])
    graph[item[1]].append(item[0]) 
    
visited = [0]*(N+1) # 한번 방문햇으면 방문처리
parent = [0]*(N+1) # 해당하는 인덱스의 부모노드에 대한 정보가 저장되있음
dfs(1)

for i in range(2,N+1):
    print(parent[i])