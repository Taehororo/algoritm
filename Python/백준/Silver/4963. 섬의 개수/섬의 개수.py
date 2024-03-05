#4963. 섬의 개수
import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    visited.append((x,y))
    #             위왼대   위      위오대   오   아오대  아    아왼대  왼
    for dx,dy in ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)):
        if 0 <= x+dx < h and 0 <= y+dy < w:
            if arr[x+dx][y+dy] == 1 and (x+dx, y+dy) not in visited:
                dfs(x+dx, y+dy)


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [] # 방문 배열
    cnt = 0 # 섬의 개수
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and (i,j) not in visited:
                dfs(i,j)
                cnt += 1
    print(cnt)