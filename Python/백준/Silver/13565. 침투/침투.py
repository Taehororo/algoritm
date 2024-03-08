#13565 침투
# 전류는 위에서만 내려온다.
# 전류가 바깥으로 아래로 나가버리면 성공 즉 x좌표아래쪽으로 넘어가면 성공

def dfs(x,y):
    global answer
    visited[x][y] =1
    for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if visited[nx][ny] == 0 and arr[nx][ny] == '0':
                dfs(nx,ny)
        elif M <= nx: # x축에서 아래로 빠져버린 경우 답은 YES
            answer = 'YES'
            return 
            
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N = map(int, input().split()) # M 높이 , N 가로
arr = [input() for _ in range(M)]#'0'은 전류통하고, '1'은 안통하고
visited = [[0]*N for _ in range(M)]
answer ='NO'
for i in range(N): 
    if arr[0][i] == '0':
        dfs(0,i)
        if answer == 'YES': # 정답이 빨리나오면 반복멈추기
            break
print(answer)
        