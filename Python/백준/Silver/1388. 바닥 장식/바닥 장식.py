# 1388. 바닥 장식

def dfs(x,y):
    visited[x][y] = 1
    if arr[x][y] == '-':
        #              왼       오
        for dy in ((-1),(1)):
            ny = y + dy
            if 0 <= ny < M and arr[x][ny] =='-' and visited[x][ny] == 0:
                dfs(x,ny)
    elif arr[x][y] == '|':
        #            위     아래
         for dx in ((-1),(+1)):
            nx = x + dx
            if 0 <= nx < N and arr[nx][y] =='|' and visited[nx][y] == 0:
                dfs(nx,y)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split()) # 세로크기 N 가로 크기 M
arr = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]

cnt = 0 # 총 판자의 개수
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i,j)
            cnt += 1 # 한번 함수를 돌때마다 판자의 개수의 총합에 더해진다.
print(cnt)