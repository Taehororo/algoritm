# 1854 K번째 최단경로 찾기
import sys,math
from heapq import heappush, heappop
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dijkstra(start):
    q = []
    heappush(q,(0,start)) 
    distance[start][0] = 0
    while q:
        dist, now = heappop(q)
        
        
        for next in graph[now]:
            next_dist = next[0]
            next_node = next[1]
            new_dist = dist+next_dist
            
            if new_dist < distance[next_node][K-1]:
                distance[next_node][K-1] = new_dist
                distance[next_node].sort()
                heappush(q,(new_dist,next_node))
            
        
N, M, K = map(int, input().split()) # n 도시 개수, m 도로 개수, k 도로
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w,e))
distance = [[math.inf for _ in range(K)] for _ in range(N+1)]
dijkstra(1)
for i in range(1,N+1):
    if distance[i][-1] == math.inf:
        print(-1)
    else:
        print(distance[i][-1])