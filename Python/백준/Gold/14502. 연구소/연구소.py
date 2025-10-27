import sys
from collections import deque
from itertools import combinations
import copy
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]


empty = []
for i in range(N):
  for j in range(M):
    if lab[i][j] == 0:
      empty.append((i,j))
      
def bfs(board):
  
  q = deque([])
  for i in range(N):
    for j in range(M):
      if board[i][j] == 2:
        q.append((i,j))
  
  while q:
    x, y = q.popleft()
    for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
      nx = x+dx
      ny = y+dy
      if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
        board[nx][ny] = 2
        q.append((nx,ny))
  return board


def safe_area(board):
  cnt = 0
  for i in range(N):
    for j in range(M):
      if board[i][j] == 0:
        cnt += 1
  return cnt

max_cnt = 0

for walls in combinations(empty,3):
  temp_lab = copy.deepcopy(lab)
  for x,y in walls:
    temp_lab[x][y] = 1
  temp_lab = bfs(temp_lab)
  max_cnt = max(max_cnt,safe_area(temp_lab))
print(max_cnt)