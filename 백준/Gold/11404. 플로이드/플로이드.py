# 플로이드 11404.py 플로이드 난 그런거몰라 다익스트라
import sys, math
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dijkstra(start):
    distance = [math.inf]*(N+1)
    distance[start] = 0
    q = []
    heappush(q,(0,start)) # 가중치, 시작위치
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

N = int(input())
M = int(input())
graph =[[] for _ in range(N+1)]

for _ in range(M):
    s, e , w = map(int, input().split())
    graph[s].append((e,w))

for i in range(1,N+1):
    answer = dijkstra(i)
    answer = answer[1:]
    for i in range(len(answer)):
        if answer[i] == math.inf:
            print(0)
        else:
            print(answer[i])