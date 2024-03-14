# 15655 N과 M(6)

def dfs(n,list):
    if n == M:
        if sorted(list) not in answer: # 정답 배열에 넣기전에 정렬해보고
            answer.append(list)        # 중복되는 것이 없다면 정답에 추가해준다.
        return
    for i in range(N):
        if arr[i] not in list:       # 한번 넣은 원소를 또 넣으면 안되기때문에
            dfs(n+1,list+[arr[i]])


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []
dfs(0,[])
for item in answer:
    print(*item)