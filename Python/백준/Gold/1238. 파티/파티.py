from heapq import heappop,heappush
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dijkstra(start):
    distance = [math.inf]*(N+1)
    q = []
    distance[start] = 0
    heappush(q,(0,start)) # weight와 마을번호
    while q:
        dist, now = heappop(q)
        if dist > distance[now]:
            continue
        for next in graph[now]:
            next_node = next[0]
            next_dist = next[1]
            new_dist = dist + next_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(q,(new_dist,next_node))
    return distance
    
    

N, M, X = map(int, input().split())
# N개의 마을 M개의 단방향 도로, X가 목적지
graph = [[] for _ in range(N+1)]
answer = [0]*(N+1)


for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e,w))

to_home = dijkstra(X)
for i in range(1,N+1):
    to_goal = dijkstra(i)
    answer[i] = to_goal[X] + to_home[i]
print(max(answer))