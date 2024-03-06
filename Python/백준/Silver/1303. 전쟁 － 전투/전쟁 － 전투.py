# 1303 전쟁-전투
import sys
sys.setrecursionlimit(10**6)

def dfs(x,y,visited,target): # x,y는 좌표, visted는 해당하는 visted 배열 , target은 누구를 찾을건지
    global cnt
    cnt += 1
    visited[x][y] = 1
    for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if arr[nx][ny] == target and visited[nx][ny] == 0:
                dfs(nx,ny,visited,target)

N, M = map(int,input().split()) # N은 전쟁터의 가로크기, M은 세로크기 
arr = [sys.stdin.readline().rstrip() for _ in range(M)] # 개행문자 /n 이 있는 문제임

our_visited = [[0]*N for _ in range(M)]
our_sum = 0 # 우리 병사의 위력 총합
enemy_visited = [[0]*N for _ in range(M)]
enemy_sum = 0 # 상대 병사의 위력 총합

for i in range(M):
    for j in range(N):# w는 우리팀 b는 상대팀
        cnt = 0
        if arr[i][j] == 'W' and our_visited[i][j] == 0:
            dfs(i,j,our_visited,'W')
            our_sum += (cnt**2)
        elif arr[i][j] == 'B' and enemy_visited[i][j] == 0:
            dfs(i,j,enemy_visited,'B')
            enemy_sum += (cnt**2)
            
print(our_sum,enemy_sum)