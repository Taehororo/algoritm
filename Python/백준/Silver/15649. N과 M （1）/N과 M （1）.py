# 15489 N과 M(1)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs():
    global answer
    if len(temp) == M:
        answer.append(temp[:]) # 많이 곤란했었다. list는 주소를 참조하기에
        #        이런식으로 [:]로 전체를 복사해서 넣어줘야한다.
        return
    for i in range(1,N+1):
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()
        


N, M = map(int, input().split())
arr = [0]*(N+1)
for i in range(1,N+1):
    arr[i] = i
temp = []
answer = []
dfs()
for item in answer:
    print(*item)