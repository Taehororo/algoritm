#1743 음식물 피하기
from pprint import pprint
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    global cnt
    cnt += 1
    visited[x][y] = 1
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N+1 and 0 <= ny < M+1:
            if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx,ny)


N, M, K = map(int, input().split()) # 세로길이 N, 가로길이 M , 음식물 쓰레기 개수 K
arr = [list(map(int, input().split())) for _ in range(K)] # r이 세로x c가 가로y
matrix = [[0]*(M+1) for _ in range(N+1)] # 위치 인덱스를 주어진대로 쓰기 위해서 그냥 배열을 한자리씩 더 추가해줌
for item in arr:
    matrix[item[0]][item[1]] = 1

max_cnt = 0
visited = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            dfs(i,j)
            max_cnt = max(cnt,max_cnt)
print(max_cnt)