#1189 컴백홈
# T는 못가는 부분, . 은 갈수있다.
# dfs
# 높이 R 가로 C 도착하는데 걸린 시간 K
# 시작점 왼쪾 아래 
# 도착점 오른쪽 위

def dfs(x,y,depth):
    global cnt
    if y == (C-1) and x == 0 and depth == K: # 집에 도착했고, 거리가 6일때
        cnt += 1 # 답 += 1
        return
    visited[x][y] = 1
    for dx,dy in ((-1,0),(+1,0),(0,-1),(0,+1)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if visited[nx][ny] == 0 and arr[nx][ny] == '.':
                visited[nx][ny] = 1 # 이것이 바로
                dfs(nx,ny,depth+1) # 백트래킹
                visited[nx][ny] = 0 # 이란 것이다.
                
R, C, K = map(int, input().split())
arr = [input() for _ in range(R)]
visited = [[0]*C for _ in range(R)]
cnt = 0
depth = 1
dfs(R-1,0,depth) # depth는 가는데 걸린 길이 시작점부터 포함하기에 거리1부터 시작
print(cnt)