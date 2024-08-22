# 1446 지름길
import sys
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dijkstra(start):
  q = []
  heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heappop(q)
    if dist > distance[now]:
      continue

    for next in graph[now]:
      next_dist = next[1]
      next_node = next[0]
      if next_node > D:
        continue
      new_dist = dist + next_dist
      if new_dist < distance[next_node]:
        if new_dist < dist + next_node-now:
          distance[next_node] = new_dist
          heappush(q,(new_dist, next_node))
        else:
          new_dist = dist + next_node-now
          distance[next_node] = new_dist
          heappush(q,(new_dist, next_node))
      elif ((dist+next_node-now) < distance[next_node]):
        new_dist = dist+next_node-now
        distance[next_node] = dist+next_node-now
        heappush(q,(new_dist, next_node))




# 지름길의 개수 N, 고속도로 길이 D
N, D = map(int, input().split())
INF = sys.maxsize
distance = [INF]*(D+1)
graph = [[] for _ in range(D+1)]
cnt = 0
for i in range(D):
  cnt += 1
  graph[i].append((i+1,cnt))

for _ in range(N):
  # 시작위치, 도착위치, 지름길의 길이
  s, e, l = map(int, input().split())
  if (s >= D):
    continue
  graph[s].append((e,l))

dijkstra(0)
print(distance[D])

