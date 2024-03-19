# 14889 스타트와 링크
import math
def dfs(idx,start,link):
    global answer
    if len(start) == L and len(link) == L:
        team_start = 0
        team_link = 0
        for x in start:
            for y in start:
                if x==y:
                    continue
                team_start += arr[x][y]
        for x in link:
            for y in link:
                if x==y:
                    continue
                team_link += arr[x][y]          
        answer = min(answer,abs(team_start-team_link))
        return
    
    if len(start) == L:
        dfs(idx+1,start,link+[idx])
    elif len(link) == L:
        dfs(idx+1,start+[idx],link)
    else:
        dfs(idx+1,start,link+[idx])
        dfs(idx+1,start+[idx],link)

N = int(input()) # N은 항상 짝수
arr = [list(map(int, input().split())) for _ in range(N)]
answer = math.inf
L = N//2 # 각팀의 맴버 숫자
dfs(0,[],[])
print(answer)