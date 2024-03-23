# 11779 최소비용 구하기 2
import math,sys
from heapq import heappop,heappush

def dijkstra(start):
    q = []
    distance[start] = 0
    heappush(q,(0,start)) # weight, 도시의 번호
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
                
                node[next_node] = now # 즉 도착점에서 쭉쭉 거슬러올라가서 출발점까지 찾을 수있는 배열
                
                heappush(q,(new_dist,next_node))

input = sys.stdin.readline
n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
graph = [[] for _ in range(n+1)]
distance = [math.inf]*(n+1)
node = [0]*(n+1) # 방문한 도시들을 저장할 정보
for _ in range(m):
    s, e, w  = map(int, input().split())
    graph[s].append([e,w])

start, goal = map(int, input().split())

dijkstra(start)
answer = []

temp = goal
while True:
    answer.append(temp)
    temp = node[temp]
    if temp == start:
        answer.append(temp)
        answer.reverse()
        break


print(distance[goal])
print(len(answer))
print(*answer)
