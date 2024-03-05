# 2606번 바이러스
def dfs(v):
    global cnt
    cnt += 1
    visited[v] = 1
    graph[v].sort
    for node in graph[v]:
        if visited[node] == 0:
            dfs(node)

N = int(input()) # 컴퓨터의 수
V = int(input()) # 직접연결되어있는 쌍의 개수
visited = [0]*(N+1)
arr = [list(map(int, input().split())) for _ in range(V)]
graph = [[] for _ in range(N+1)]
for item in arr: # 단방향이라는 얘기가 없으니 양쪽에서 갈수있으니 추가해준다.
    graph[item[0]].append(item[1])
    graph[item[1]].append(item[0])
cnt = -1 # 감염된 컴퓨터의 개수 처음에 시작한 컴퓨터도 포함되기에 제거해준다.
# print(graph) # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
#             # 이런식으로 각 정점마다 연결되어있는 정점 확인 가능

dfs(1) # 1번 정점부터 시작
print(cnt)
