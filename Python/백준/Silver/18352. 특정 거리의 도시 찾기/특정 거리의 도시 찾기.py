import sys
import math
from heapq import heappop,heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dijkstra(start):
    q= []
    distance[start] = 0
    heappush(q,(0,start)) # 가중치와, 도시번호
    while q:
        dist, now = heappop(q)
        if dist > distance[now]:
            continue
        for next in graph[now]:
            next_node = next
            next_dist = 1
            new_dist = dist + next_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(q,(new_dist,next_node))
                
                
N, M, K, X = map(int, input().split())
# 도시의 개수 N, 도로의 개수 M 단방향, 거리가 K인 답 출력, 출발 도시 X
distance = [math.inf]*(N+1) # 0번 도시는 없어요
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e) # 거리의 가중치가 전부 1이기에 걍 노드만 넣음
    
dijkstra(X)

boolen = True
for i in range(1,N+1):
    if distance[i] == K:
        print(i)
        boolen = False
if boolen: # K 거리가 없을 경우
    print(-1)