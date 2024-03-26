# 2178 미로탐색
import sys
from collections import deque
from pprint import pprint 
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# def dfs(x,y,depth):
#     global answer
#     if x == N-1 and y == M-1:
#         answer = min(answer,depth)
#         return
    
#     for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
#         nx = x + dx
#         ny = y + dy
#         if 0 <= nx < N and 0 <= ny < M:
#             if visited[nx][ny] == 0 and arr[nx][ny] =='1':
#                 visited[nx][ny] = 1
#                 dfs(nx,ny,depth+1)
#                 visited[nx][ny] = 0

# dfs는 시간초과가 자꾸나!!!!!!!

def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)): 
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx,ny))
  
                
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
bfs(0,0)
print(arr[N-1][M-1])