#10971 외판원 순회2
def dfs(n,cost,depth): # 현재 있는 도시의 위치, 현재까지의 비용, 몇번째 도시인지
    global answer
    global start
    if cost >= answer: # 기존의 최소거리보다 멀다면 그냥 종료
        return
    if depth == N:  # 한바퀴 돌았을때
        if n == start: # 출발점으로 돌아왔다면
            answer = min(answer,cost) # 기존 정답과 비교
        return 
    for i in range(N):
        if visited[i] == 0 and arr[n][i] > 0:
            visited[i] = 1            
            dfs(i,cost + arr[n][i],depth+1)
            visited[i] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 10000001
for i in range(N):
    visited = [0]*(N)
    start = i 
    dfs(i,0,0)
print(answer)