import sys
from collections import deque
from pprint import pprint
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
time = 0

def melting_air(arr):
  i,j = 0,0
  arr[i][j] -= 1
  visited = [[-1]*M for _ in range(N)]
  visited[i][j] = 0
  q = deque([(i,j)])
  while q:
    x,y = q.popleft()
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
      nx = x + dx
      ny = y + dy
      if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] <= 0 and visited[nx][ny] == -1:
        visited[nx][ny] = 1
        arr[nx][ny] -= 1
        q.append((nx,ny))

def is_melting(x,y):
  cnt = 0
  for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
    nx = x + dx
    ny = y + dy
    if 0 <= nx < N and 0 <= ny < M:
      if board[nx][ny] != 1 and board[nx][ny] != 0:
        cnt += 1
  if cnt >= 2:
    return True
  else:
    return False

def any_cheese(arr):
  for i in range(N):
    for j in range(M):
      if arr[i][j] == 1:
        return True
  
  return False

if not any_cheese(board):
  print(0)

else: 
  while True:
    time += 1
    cheese = []
    melting_air(board)
    for i in range(N):
      for j in range(M):
        if board[i][j] == 1:
          cheese.append((i,j))
    for x, y in cheese:
      melting = is_melting(x,y)
      if melting:
        board[x][y] = 0
    
    if any_cheese(board):
      continue
    break
  print(time)