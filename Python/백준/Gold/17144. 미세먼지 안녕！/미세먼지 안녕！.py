import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

# 청정기 위치
clener = []
for i in range(R):
  if board[i][0] == -1:
    clener.append((i,0))
  


def dust(air):
  temp_air = copy.deepcopy(air)
  for i in range(R):
    for j in range(C):
      # 확산이 일어나는 조건
      if air[i][j] >= 5:
        x, y = i, j
        # 4방향중 확산된 수
        cnt = 0
        for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
          nx = x + dx
          ny = y + dy
          if 0 <= nx < R and 0 <= ny < C and air[nx][ny] != -1:
            cnt += 1
            temp_air[nx][ny] += air[x][y] // 5
        temp_air[x][y] -= (air[x][y] // 5)*cnt
  return temp_air

def clean_1(air):
  temp_air = copy.deepcopy(air)
  x1, y1 = clener[0]
  # 청정기 바로 옆부터 시작해야 해서
  y1 += 1
  temp_air[x1][y1] = 0
  while True:
    ny = y1 + 1
    if 0 <= ny < C:
      temp_air[x1][ny] = air[x1][y1]
      y1 = ny
    else:
      break
  while True:
    nx = x1 - 1
    if 0 <= nx < R:
      temp_air[nx][y1] = air[x1][y1]

      x1 = nx
    else:
      break
  while True:
    ny = y1 -1
    if 0 <= ny < C:
      temp_air[x1][ny] = air[x1][y1]

      y1 = ny
    else:
      break
  while True:
    nx = x1 + 1
    if 0 <= nx < R and air[nx][y1] != -1:
      temp_air[nx][y1] = air[x1][y1]

      x1 = nx
    else:
      break
  return temp_air

def clean_2(air):
  temp_air = copy.deepcopy(air)
  x2, y2 = clener[1]
  # 청정기 바로 옆부터 시작해야 해서
  y2 += 1
  temp_air[x2][y2] = 0
  while True:
    ny = y2 + 1
    if 0 <= ny < C:
      temp_air[x2][ny] = air[x2][y2]
      y2 = ny
    else:
      break
  while True:
    nx = x2 + 1
    if 0 <= nx < R:
      temp_air[nx][y2] = air[x2][y2]

      x2 = nx
    else:
      break
  while True:
    ny = y2 -1
    if 0 <= ny < C:
      temp_air[x2][ny] = air[x2][y2]

      y2 = ny
    else:
      break
  while True:
    nx = x2 - 1
    if 0 <= nx < R  and air[nx][y2] != -1:
      temp_air[nx][y2] = air[x2][y2]

      x2 = nx
    else:
      break
  return temp_air 


def cnt_dust(air):
  cnt = 0
  for i in range(R):
    for j in range(C):
      if air[i][j] > 0:
        cnt += air[i][j]
  return cnt

for _ in range(T):
  board = dust(board)
  board = clean_1(board)
  board = clean_2(board)
print(cnt_dust(board))