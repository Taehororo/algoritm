from heapq import heappop,heappush 
import math

def dijkstra(start):
    q = []
    distance[start] = 0 # 자기자신은 0이지 암
    heappush(q,(0,start)) # q에다가 wegiht와 도시번호 넣어버리깅 이 순서 매우중요!
                            # 이 w기준으로 heapq 가 되기때문이지요
    while q:
        dist, now = heappop(q)
        
        if dist > distance[now]:
            continue
        
        for next in graph[now]:
            next_wegiht = next[1]
            next_node = next[0]
            new_wegiht = dist + next_wegiht
            if new_wegiht < distance[next_node]:
                distance[next_node] = new_wegiht
                heappush(q,(new_wegiht,next_node))
                


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)] # 0번 도시는 없답니다람쥐
distance = [math.inf]*(N+1) # 0번 도시는 없다
for _ in range(M):
    s, e , w = map(int, input().split())
    graph[s].append((e,w))

start, goal = map(int, input().split())
dijkstra(start)
print(distance[goal])