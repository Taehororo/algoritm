import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

sx, sy = 0, 0 
for i in range(N):
  for j in range(N):
    if board[i][j] == 9:
      sx,sy = i, j
      board[i][j] = 0
size = 2 
exp = 0
time = 0
def bfs(x,y, size):
  visited = [[-1]*N for _ in range(N)]
  visited[x][y] = 0 
  q = deque([(x,y)])
  fish = []
  
  while q:
    cx, cy = q.popleft()
    for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
      nx, ny = cx + dx, cy + dy
      if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
        if board[nx][ny] <= size:
          visited[nx][ny] = visited[cx][cy] + 1
          q.append((nx,ny))
          if 0 < board[nx][ny] < size:
            fish.append((visited[nx][ny],nx,ny))
            
  if not fish:
    return None
  fish.sort()
  return fish[0]


while True:
  target = bfs(sx,sy, size)
  if target is None:
    break
  dist, nx, ny = target
  time += dist
  board[nx][ny] = 0
  sx, sy = nx, ny
  exp += 1
  if exp == size:
    size += 1
    exp =0
    
print(time)