from itertools import combinations
from collections import deque
import copy

# 입력
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 빈칸 위치 찾기
empty = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]

# BFS로 바이러스 확산
def spread_virus(board):
    q = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
    return board

# 안전 영역 계산
def safe_area(board):
    return sum(row.count(0) for row in board)

max_safe = 0

# 모든 벽 조합 시뮬레이션
for walls in combinations(empty, 3):
    temp_lab = copy.deepcopy(lab)
    for x, y in walls:
        temp_lab[x][y] = 1
    temp_lab = spread_virus(temp_lab)
    max_safe = max(max_safe, safe_area(temp_lab))

print(max_safe)
