import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]


def bfs(board):
  visited = [[-1]*M for _ in range(N)]
  visited[0][0] = 1
  q = deque([(0,0)])
  
  while q:
    x, y = q.popleft()
    if x == N-1 and y == M-1:
      break
    for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
      nx = x + dx
      ny = y + dy
      if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and board[nx][ny] =='1':
        q.append((nx,ny))
        visited[nx][ny] = visited[x][y] + 1
  return visited[N-1][M-1]

print(bfs(arr))
