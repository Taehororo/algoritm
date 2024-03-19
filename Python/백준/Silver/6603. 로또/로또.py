#6603 로또
def dfs(n,lst):
    if n == 6:
        lst.sort()
        if lst not in answer:
            answer.append(lst)
        return
    p = 0
    for i in range(n,k):
        if p!= S[i]:
            p = S[i]
            if v[i] == 0:
                v[i] = 1
                dfs(n+1,lst+[S[i]])
                v[i] = 0
        else:
            continue
        
while True:
    # S = list(map(int, input().split()))
    # k = S[0]
    # if k == 0:
    #     break
    # S = S[1:]
    
    k, *S = list(map(int, input().split()))
    if k == 0:
        break
    # 이 k의 길이를 가진 S 리스트안에서 6개만 고르는 것이다.
    answer = []
    v = [0]*k
    dfs(0,[])
    for item in answer:
        print(*item)
    print()