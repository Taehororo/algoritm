# 15651 N과 M(3)

def dfs(n,lst):
    if n == M:
        answer.append(lst)
        return
    for i in range(1,N+1):
        dfs(n+1,lst+[i])
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

answer = []
dfs(0,[])
for item in answer:
    print(*item)
