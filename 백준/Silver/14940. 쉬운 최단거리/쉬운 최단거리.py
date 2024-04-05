# 14940 쉬운 최단거리 
# 나는 다익스트라로 풀어야지
import sys,math
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(x,y):
    q = []
    distance[x][y] = 0
    heappush(q,(distance[x][y],x,y))# 가중치, x,y

    while q:
        dist, x,y = heappop(q)
        if dist > distance[x][y]:
            continue

        for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0:
                next_dist = dist + arr[nx][ny]
                if next_dist < distance[nx][ny]:
                    distance[nx][ny] = next_dist
                    heappush(q,(next_dist,nx,ny))




N, M = map(int,input().split()) # 세로 n, 가로 m

arr = [list(map(int, input().split())) for _ in range(N)]
distance = [[math.inf]*M for _ in range(N)]

x = 0
y = 0 
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            x=i
            y=j
            break


dijkstra(x,y)
for i in range(N):
    for j in range(M):
        if distance[i][j] == math.inf: 
            if arr[i][j] ==0:
                print(0,end=' ')
            else:
                print(-1,end=' ')
        else:
            print(distance[i][j],end=' ')
    print()