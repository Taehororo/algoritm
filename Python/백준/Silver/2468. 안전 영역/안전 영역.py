# 2468. 안전 영역
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
def bfs(x,y):
    visited[x][y] = 1
    queue = deque([(x,y)])
    while queue:
        loc = queue.popleft()     
        for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
            nx, ny = loc[0] + dx, loc[1] + dy
            if 0<= nx < N and 0<= ny < N and visited[nx][ny] == 0 and  arr[nx][ny] >rain:
                queue.append((nx,ny))
                visited[nx][ny] = 1
        
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_val = 101 # 가장 낮은 기둥의 높이
max_val = 0 # 가장 높은 기둥의 높이
max_cnt = 1 # 가장 많은 안전한 영역의 개수 # 비가 아예 안올때를 대비한 1
for i in range(N):
    min_val = min(min_val,min(arr[i])) # 가장 낮은 기둥높이 찾기
    max_val = max(max_val,max(arr[i])) # 가장 높은 기둥높이 찾기



for rain in range(min_val,max_val): # 비가 오는 경우는 가장낮은 높은 기둥의 수부터, 가장 높은 기둥의 수 전까지 하면된다
    visited = [[0]*N for _ in range(N)]
    cnt = 0 # 안전한 영역의 개수
    for i in range(N):
        for j in range(N):
            if arr[i][j] >rain and visited[i][j] == 0: # 잠긴 영역이 아니라면
                bfs(i,j)                                 # 함수 돌기
                cnt += 1
    max_cnt = max(max_cnt,cnt)
print(max_cnt)