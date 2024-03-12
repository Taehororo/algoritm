# 15650. N과 M(2)

def dfs(depth):
    if len(temp) == M:
        answer.append(temp[:])
        return
    for i in range(depth,N+1):
        if i not in temp:
            temp.append(i)
            dfs(i+1)
            temp.pop()
        

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = [0]*(N+1)
for i in range(N+1):
    arr[i] = i 

answer =[]
temp = []
dfs(1)
for item in answer:
    print(*item)