import sys,math
from heapq import heappush,heappop
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dijkstra(start): # 시작하는 위치와, 그 시작하는 위치의 가중치
    q = []
    distance[start] = 0
    heappush(q,(0,start))
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            next_dist = next[0]
            next_node = next[1]
            new_dist = dist + next_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(q,(new_dist,next_node))
    


N, M = map(int,input().split()) # n개의 헛간, m개의 길
graph = [[] for _ in range(N+1)] # 그래프
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w,e))
    graph[e].append((w,s))
    
distance = [math.inf]*(N+1)
dijkstra(1) # 시작하는 위치
print(distance[N])