# 1697 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(x): # 시작하는 위치 x
    q = deque([x])
    while q:
        now = q.popleft()
        if now == K:
            return visited[now]
        for next in (now-1,now+1,now*2):
            if 0 <= next <= 100000 and visited[next] == 0:
                visited[next] = visited[now] + 1
                q.append(next)


N, K = map(int, input().split())
visited = [0]*100001
print(bfs(N))