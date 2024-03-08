# 16173. 점프왕 쩰리(small)
# 젤리 시작점 가장 왼쪽위
# 오른쪽과 아래로만 이동가능
# 가장 오른쪽아래 도착점
def dfs(x,y):
    global answer
    visited[x][y] = 1
    for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
        nx = x + arr[x][y] * dx
        ny = y + arr[x][y] * dy
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == -1: # 도착지에 도착한 경우 답은 하루하루
                answer = 'HaruHaru'
                return
            if visited[nx][ny] == 0:
                dfs(nx,ny)


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
answer = 'Hing' # 기본적으론 답을 Hing이라고 설정
dfs(0,0)
print(answer)