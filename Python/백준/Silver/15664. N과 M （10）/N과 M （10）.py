# 15664 N과 M (10)


def dfs(n,list,idx):
    if n == M:
        list.sort()
        if list not in answer:
            answer.append(list)
        return
    for i in range(n,N):
        if i not in idx:
            dfs(n+1,list+[arr[i]],idx+[i])
        


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []
dfs(0,[],[])

for item in answer:
    print(*item)