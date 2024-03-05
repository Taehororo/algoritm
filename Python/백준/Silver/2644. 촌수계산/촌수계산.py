import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(s, t, depth): # depth를 추가하여 촌수를 계산합니다.
    global cnt
    global check
    if s == t: # 원하는 타겟에 도달하면 촌수를 cnt에 기록하고 플래그를 True로 설정합니다.
        check = True
        cnt = depth
        return    
    visited[s] = True
    for node in graph[s]:
        if check: # 플래그가 True이면 종료합니다.
            return
        if not visited[node]:
            dfs(node, t, depth + 1) # 다음 정점으로 이동하며 depth를 1 증가시킵니다.

N = int(input()) # 전체 사람의 수
t1, t2 = map(int, input().split()) # 촌수를 계산해야하는 두 사람
m = int(input()) # 부모 자식들 간의 관계의 개수
arr = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for item in arr:
    graph[item[0]].append(item[1])
    graph[item[1]].append(item[0])

check = False
cnt = 0
dfs(t1, t2, 0) # depth를 0으로 초기화하여 시작합니다.
if check:
    print(cnt)
else:
    print('-1')