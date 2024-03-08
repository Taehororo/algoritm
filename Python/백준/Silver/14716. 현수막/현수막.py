# 14716 현수막

def dfs(x,y):
    visited[x][y] = 1
    #           위왼 위 위오 오 밑오 밑 밑왼 왼
    for dx, dy in ((-1,-1),(-1,0),(-1,+1),(0,+1),(+1,+1),(1,0),(1,-1),(0,-1)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if visited[nx][ny] == 0 and arr[nx][ny] == 1:
                dfs(nx,ny)
            
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N = map(int, input().split()) # M은 높이, N은 가로
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
cnt = 0 # 글자수
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j)
            cnt += 1
print(cnt)