#15900 나무 탈출
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(500000)
def dfs(v,depth):
    root[v] = depth
    visited[v] =1
    for node in graph[v]:
        if visited[node] == 0:
            dfs(node,depth+1)
            
    
N = int(input()) # 정점의 개수 N
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1) # 방문배열
root = [0]*(N+1) # 노드의 깊이를 의미
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


depth = 0
cnt = 0
dfs(1,depth)
for i in range(2,N+1): # 1은 머리이기때문에 제외하고 만약 연결된 노드가 1개라면, 즉 뿌리
                        # 왜냐면 배열에 양방향으로 넣어줬기 때문에
    if len(graph[i]) == 1:
        cnt += root[i] # 전체 길이에 추가해준다.

if cnt % 2 == 0:
    print('No')
else:
    print('Yes')