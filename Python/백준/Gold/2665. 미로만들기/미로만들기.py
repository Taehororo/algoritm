import math,sys
from heapq import heappop,heappush
from collections import deque
# from pprint import pprint as pprint
# def bfs(x,y):
#     q = deque([])
#     q.append((x,y))
#     visited = [[0]*N for _ in range(N)]
#     visited[x][y] = 1
#     while q:
#         r, c = q.popleft()       
#         for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
#             nx = r + dx
#             ny = c + dy
#             if 0 <= nx < N and 0 <= ny< N and arr[nx][ny] == 1:
#                 if visited[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     arr[nx][ny] = 0
#                     q.append((nx,ny))
                
    

def dijkstra():
    q= []
    distance[0][0] = 0
    heappush(q,(0,0,0)) # weihgt, x, y
    while q:
        dist, x, y = heappop(q)
        
        if dist > distance[x][y]:
            continue
        
        for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny< N:
                if dist + arr[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = dist + arr[nx][ny]
                    heappush(q,(distance[nx][ny],nx,ny))
                    # if arr[nx][ny] == 1:
                    #     bfs(nx,ny)





N = int(input())
arr = [list(map(str, input())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            arr[i][j] = 0
        else:
            arr[i][j] = 1

distance = [[math.inf]*N for _ in range(N)]
# pprint(arr)

dijkstra()
# pprint(distance)
print(distance[-1][-1])

