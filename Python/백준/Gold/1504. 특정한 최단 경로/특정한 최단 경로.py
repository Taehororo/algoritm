from heapq import heappop,heappush
import math,sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dijkstra(start):
    distance= [math.inf]*(N+1)
    q = []
    distance[start] = 0
    heappush(q,(0,start)) # weight와 노드번호
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

N, E = map(int, input().split())# 정점의 개수 N, 간선의 개수 E
graph = [[] for _ in range(N+1)]


for _ in range(E):
    s, e , w = map(int, input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

goal1, goal2 = map(int, input().split())

answer1 = 0
answer2 = 0

answer1 += dijkstra(1)[goal1]
answer2 += dijkstra(1)[goal2]

answer1 += dijkstra(goal1)[goal2]
answer2 += dijkstra(goal2)[goal1]

answer1 += dijkstra(goal2)[N]
answer2 += dijkstra(goal1)[N]

answer = min(answer1,answer2)
if answer == math.inf:
    print(-1)
else:
    print(answer)