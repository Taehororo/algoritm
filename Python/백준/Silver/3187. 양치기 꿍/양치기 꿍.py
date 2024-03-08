# 3187 양치기 꿍
# 아니 3184번이랑 다르게 그냥 양의 기호가 o 에서 k로 바뀐거밖에없자나
def dfs(x,y,kind): # x좌표,y좌표, kind 종류
    global s_cnt # 요번 우리 안에 있는 양의 개수
    global w_cnt # 요번 우리 안에 있는 늑대의 개수
    if kind == 'k':
        s_cnt += 1
    elif kind =='v':
        w_cnt += 1
    visited[x][y] = 1
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,+1)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < R and 0<= ny < C and visited[nx][ny] == 0:
            if arr[nx][ny] != '#': # 목장울타리만 아니면 통과!
                dfs(nx,ny,arr[nx][ny])
                
    

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

R, C = map(int, input().split()) # R 높이 C는 가로
arr = [input() for _ in range(R)]
wolf = 0 # 총 늑대 개수
sheep = 0 # 총 양 개수
visited = [[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if visited[i][j] == 0: # 방문한적이 없다면
            if arr[i][j] == 'k' or arr[i][j] =='v':
                s_cnt = 0 # 요번우리 안에 있는 양의 개수
                w_cnt = 0 # 요번우리 안에 있는 양의 개수
                dfs(i,j,arr[i][j])
                if s_cnt > w_cnt: # 요번 우리 안에 양이 더 많을때
                    sheep += s_cnt
                else:             # 요번 우리 안에 늑대가 더 많을때
                    wolf += w_cnt 
print(sheep,wolf)
