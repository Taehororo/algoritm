# 15657 N과 M (8)

def dfs(n,list):
    if n == M:
        answer.append(list)
        return
    for i in range(N):
        try:  #  처음에 넣을때 -1때문에 인덱스 에러가 나 꼼수를 부림
            # try excepy 쓰기 싫으면 그냥 밑에 함수에 [0] 넣고
            # 나중에 출력할때 0번 인덱스 빼버리거나 answer에 append할때
            # 빼고 넣는 방법 등이 있다.
            if arr[i] >= list[-1]: # 전에 넣은 것보다 크거나 같은경우에만 허용
                dfs(n+1,list+[arr[i]])
        except:
            dfs(n+1,list+[arr[i]])

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []
dfs(0,[])

for item in answer:
    print(*item)