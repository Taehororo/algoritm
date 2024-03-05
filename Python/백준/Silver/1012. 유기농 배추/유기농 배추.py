# 1012 유기농배추
import sys
sys.setrecursionlimit(100000)
from collections import deque
def find_path(x,y):
    visited.append((x,y))
    #               위    아래    오른쪽   왼쪽
    for dx,dy in ((-1,0),(+1,0),(0,+1),(0,-1)):
        if 0<= x+dx < N and 0 <= y+dy < M:
            if matrix[x+dx][y+dy] == 1 and (x+dx,y+dy) not in visited:
                find_path(x+dx,y+dy)

T = int(input())
for _ in range(1, T+1):
    M, N, K = map(int, input().split()) # 배추밭 가로길이M, 배추밭 세로길이N, 배추개수 K
    arr = [list(map(int, input().split())) for _ in range(K)]
    matrix = [[0] * M for _ in range(N)]
    # 주어진 입력이 x와 y가 반대인것 생각해라
    for item in arr:
        matrix[item[1]][item[0]] = 1

    visited = deque([]) # 방문했는지 확인
    cnt = 0 # 필요한 배추벌레의 개수
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and (i,j) not in visited: # 새로운 그룹일때
                find_path(i,j) # 배추벌레가 갈수잇는데까지 간다
                cnt += 1 # 필요한 배추벌레 개수 한개 추가
    print(cnt)