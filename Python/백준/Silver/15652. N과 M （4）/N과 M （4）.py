# 15652 N과 M(4)

def dfs(n,arr):
    if n == M+1:
        ans.append(arr)
        return
    for i in range(1,N+1):
        # try except을 써준 이유는 맨처음 빈공간에 처음 넣을때 인덱스 에러가 발생하기에
        # 다음과 같은 꼼수를 이용하였다.
        try:
            if i >= arr[-1]:
                dfs(n+1,arr+[i])
        except:
            dfs(n+1,arr+[i])

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

ans = []
dfs(1,[])
for item in ans:
    print(*item)