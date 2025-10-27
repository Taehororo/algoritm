from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 아기 상어 초기 위치
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            sx, sy = i, j
            graph[i][j] = 0

size = 2
exp = 0
time = 0

def bfs(x, y, size):
    visited = [[-1]*N for _ in range(N)]
    visited[x][y] = 0
    q = deque([(x, y)])
    fish = []

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if graph[nx][ny] <= size:
                    visited[nx][ny] = visited[cx][cy] + 1
                    q.append((nx, ny))
                    if 0 < graph[nx][ny] < size:
                        fish.append((visited[nx][ny], nx, ny))
    
    if not fish:
        return None
    fish.sort()  # 거리, x, y 순으로 정렬 (위, 왼쪽 우선)
    return fish[0]

while True:
    target = bfs(sx, sy, size)
    if target is None:
        break
    dist, nx, ny = target
    time += dist
    graph[nx][ny] = 0
    sx, sy = nx, ny
    exp += 1
    if exp == size:
        size += 1
        exp = 0

print(time)
