# 15656 N과 M(7)

def dfs(n,list):
    if n == M:

        answer.append(list)
        return
    for i in range(N): # 요번엔 중복 허용
        dfs(n+1,list+[arr[i]])
        
    

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort() # 오름차순이니까
answer = []
dfs(0,[])

for item in answer:
    print(*item)