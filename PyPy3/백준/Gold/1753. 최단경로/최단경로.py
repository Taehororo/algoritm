# 1753. 최단경로
import sys
from heapq import heappop,heappush

def dijkstra(start):
    q = []
    heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist, now = heappop(q)
        
        if dist > distance[now]:
            continue
        
        for next in graph[now]:
            next_dist = next[1]
            next_node = next[0]
            new_dist = dist + next_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(q,(new_dist,next_node))
    

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
INF = sys.maxsize
distance = [INF] * (V+1)
for _ in range(E):
    s, e , w = map(int, input().split())
    graph[s].append((e,w))
    
dijkstra(start)

for dist in distance[1:]:
    if dist == INF:
        print('INF')
    else:
        print(dist)
    