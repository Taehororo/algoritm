from heapq import heappop,heappush
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dijkstra(start):
    q = []
    distance[start] = 0 
    heappush(q,(0,start))
    
    while q:
        dist, now = heappop(q)
        if dist > distance[now]:
            continue
        
        for dx in ((now-1,1),(now+1,1),(now*2,0)):
            next_node = dx[0]
            next_dist = dx[1]
            new_dist = dist + next_dist
            if 0<= next_node <= 100000 and new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(q,(new_dist,next_node))

start, goal = map(int, input().split())
distance = [math.inf]*(100001)

dijkstra(start)
print(distance[goal])