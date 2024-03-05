# 1325. 효율적인 해킹
import sys
from collections import deque
input = sys.stdin.readline
def bfs(v):
    global cnt
    queue = deque([v])
    visited[v] = 1
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if not visited[n]: # 방문하지않았으면
                queue.append(n)
                visited[n] = 1
                cnt += 1

N, M = map(int, input().split()) # N은 컴터의 개수 M 은 간선의 개수
graph = [[] for _ in range(N+1)]
graph = deque(graph)
for _ in range(M):
    i,j = map(int, input().split())
    graph[j].append(i)

max_cnt = 0 # 지금까지 가장 많이 갈수잇는 기록의 경로 수
computer = [] # 가장 많이 갈수있는 컴퓨터의 번호가 저장된 배열
for i in range(1,N+1):
    if not graph[i]: # 연결안되어있는 애들은 시작도안하게설정
        continue
    cnt = 0
    visited = [0]*(N+1)
    bfs(i)
    if cnt > max_cnt: # 가장 많이 갈 수있는게 갱신되었다면w
        computer = []
        max_cnt = cnt
        computer.append(i)
    elif cnt == max_cnt: # 현재 가장 많이 갈수잇는거랑 같다면
        computer.append(i)

print(*computer)