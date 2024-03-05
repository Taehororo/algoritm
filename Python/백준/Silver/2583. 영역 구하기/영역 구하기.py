# 2583. 영역 구하기
from pprint import pprint
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    global sum
    sum += 1
    visited[x][y] = 1
    for dx,dy in ((-1,0),(+1,0),(0,-1),(0,+1)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if matrix[nx][ny]== 0 and visited[nx][ny] == 0:
                dfs(nx,ny)     

M, N, K = map(int, input().split()) # M 은 높이 N은 너비 K는 직사각형 개수
# x와 y를 거꾸로 생각하자
arr = [list(map(int, input().split())) for _ in range(K)]
matrix = [[0]*N for _ in range(M)]
# 뒤에거에 -1 하자
cnt = 0 # 분리된 영역의 숫자
area =[] # 각 분리된 영역의 넓이 나중에 sort하고 출력해야함
for item in arr:
    for i in range(item[1],item[3]):
        for j in range(item[0],item[2]):
            matrix[i][j] = 1
visited = [[0]*N for _ in range(M)] # 방문 배열

for i in range(M):
    for j in range(N):
        if matrix[i][j] == 0 and visited[i][j] == 0:
            sum = 0  # 해당하는 영역의 넓이
            dfs(i,j)
            cnt += 1 # 분리된 영역의 개수
            area.append(sum)

print(cnt)
area.sort() # 오름차순으로 정렬
for item in area:
    print(item, end=' ')