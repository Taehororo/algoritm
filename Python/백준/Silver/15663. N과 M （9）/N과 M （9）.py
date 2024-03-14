def dfs(n,list):
    if n == M:
        answer.append(list)
        return
    p = 0
    for i in range(N):
        if v[i] == 0 and p!=arr[i]:
            p = arr[i]
            v[i]=1
            dfs(n+1,list+[arr[i]])
            v[i]=0
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []
v = [0]*N
dfs(0,[])

for item in answer:
    print(*item)