def dfs(n,list):
    if n == M:
        answer.append(list)
        return
    p = 0  # 중복되는 값 안넣을려고 설정
    for i in range(N):
        if p != arr[i]:
            p = arr[i]
            if len(list) == 0:
                dfs(n+1,list+[arr[i]])
            else:
                if arr[i] >= list[-1] : # 넣을 수 있는 조건인지확인
                    dfs(n+1,list+[arr[i]])
                    


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
v = [0]*N
answer = []
dfs(0,[])
for item in answer:
    print(*item)