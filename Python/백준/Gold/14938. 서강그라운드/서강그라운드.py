# 14938 서강그라운드
import math,sys
from heapq import heappop,heappush
input = sys.stdin.readline

def dijkstra(start):
    distance[start] = 0 
    q = []
    heappush(q,(0,start)) # weight,와 지역번호
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
    

n, m , r = map(int, input().split())
# 지역의 개수 n , 수색범위, m 길의 개수 r 
item = [0]+list(map(int, input().split()))
# 각 구역의 아이템의 수
graph = [[] for _ in range(n+1)]

for _ in range(r):
    s, e , w = map(int, input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

answer = 0
for i in range(1,n+1):
    distance = [math.inf]*(n+1)
    dijkstra(i)
    temp = 0
    for j in range(1,n+1):   
        if distance[j] <= m:
            temp += item[j]
    answer = max(answer,temp)
print(answer)