# 15653 N과 M(5)

def dfs(n,list):
    if n == M:
        answer.append(list)
        return
    for i in range(N):
        if arr[i] not in list: # 똑같은 걸 또 넣으면 안되닝께
            dfs(n+1,list+[arr[i]])


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort() # 오름차순이니께

answer = []
dfs(0,[])
for item in answer:
    print(*item)