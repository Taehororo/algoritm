# 7569.py 토마토

# 상자의 가로 M 세로 N 높이 H
# 1은 익은 토마토, 0은 익지않은 토마토, -1은 노토마토
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

queue = deque()

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

M, N, H = map(int, input().split())
answer_flag = False
arr = []
for _ in range(H):
  temp_arr = [list(map(int, input().split())) for _ in range(N)]
  arr.append(temp_arr)
visited = [[[0]*M for _ in range(N)] for _ in range(H)]

answer = 0

def bfs():
  while queue:
    x, y, z  = queue.popleft()
    for i in range(6):
      nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
      if nx < 0 or M <= nx or ny < 0 or N <= ny or nz < 0 or H <= nz:
        continue

      if arr[nz][ny][nx] == 0 and visited[nz][ny][nx] == 0:
        visited[nz][ny][nx]=1
        arr[nz][ny][nx] = arr[z][y][x] + 1
        queue.append((nx,ny,nz))


for i in range(H):
  for j in range(N):
    for z in range(M):
      if arr[i][j][z] == 1:
        queue.append((z,j,i))
bfs()

for a in arr:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)            
        answer = max(answer, max(b))

    
print(answer-1)




