import math,sys
from heapq import heappop,heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dijkstra():
    q = []
    distance[0][0] = arr[0][0]
    heappush(q,(arr[0][0],0,0)) # weight, x좌표,y좌표
    
    
    while q:
        dist, x, y = heappop(q)
        
        if dist > distance[x][y]:
            continue
        
        for dx, dy in((-1,0),(1,0),(0,1),(0,-1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                next_dist = dist + arr[nx][ny]
                if next_dist < distance[nx][ny]:
                    distance[nx][ny] = next_dist
                    heappush(q,(next_dist,nx,ny))
    

i = 0
while True:
    i += 1
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[math.inf]*N for _ in range(N)]
    dijkstra()
    
    print(f'Problem {i}: {distance[-1][-1]}') 