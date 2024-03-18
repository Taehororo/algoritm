def dfs(n,list):
    if n == M:
        answer.append(list)
        return
    p = 0
    for i in range(N):
        if p!=arr[i]:
            p = arr[i]
            dfs(n+1,list+[arr[i]])


N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
answer = []
dfs(0,[])
for item in answer:
    print(*item)