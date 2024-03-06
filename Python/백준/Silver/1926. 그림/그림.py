# 1926 그림
def dfs(x,y):
    global cnt
    cnt += 1
    visited[x][y] = 1
    # 위, 아래, 왼, 오
    for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
        nx = x+dx
        ny = y+dy
        if 0 <= nx < N and 0<= ny < M and visited[nx][ny] == 0 and arr[nx][ny] == 1:
            dfs(nx,ny)
    pass

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # pypy에선 지나치겐 깊게 설정할경우 런타임 에러뜸
N, M = map(int, input().split()) # N 세로크기 M은 가로크기
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
num = 0 # 그림의 개수
max_cnt = 0 # 가장 넓은 그림의 그림

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt = 0 # 해당하는 그림의 넓이
            dfs(i,j)
            num += 1 # 한번 씩 이렇게 찾을때마다 그림의 개수 늘어나고
            max_cnt = max(cnt,max_cnt) # 현재 그림의 넓이를 체그한후 가장 큰 그림의 값을 저장
print(num)
print(max_cnt)