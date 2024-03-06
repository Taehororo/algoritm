# 2210. 숫자판 점프

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y,temp):
    if len(temp) == 6:
        if temp not in answer:
            answer.append(temp) # 만약 길이가 6이고 여태까지 없었던 조합이라면 정답에 추가
        return

    for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0<= ny < N:
            dfs(nx,ny,temp+arr[nx][ny])
        

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
N = 5 # 숫자판의 가로,세로 길이
arr = [list(map(str, input().split())) for _ in range(N)]

answer = [] # 정답인 애들이 들어가 있는 리스트
for i in range(N):
    for j in range(N):
        dfs(i,j,arr[i][j])
print(len(answer))