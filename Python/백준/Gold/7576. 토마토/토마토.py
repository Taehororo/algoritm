import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def tomato(board):
  q = deque([])
  v = [[-1]*M for _ in range(N)]
  for i in range(N):
    for j in range(M):
      if board[i][j] == 1:
        q.append((i,j))
        v[i][j] = 0
        
  while q:
    x, y = q.popleft()
    for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
      nx = x + dx
      ny = y + dy
      if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and v[nx][ny] == -1:
        board[nx][ny] = 1
        v[nx][ny] = v[x][y] +1
        q.append((nx,ny))
  return v


visited = tomato(board)
flag = True
for i in range(N):
  for j in range(M):
    if board[i][j] == 0:
      answer = -1
      flag = False
      

if flag:
  for i in range(N):
    answer = max(answer,max(visited[i]))
print(answer)