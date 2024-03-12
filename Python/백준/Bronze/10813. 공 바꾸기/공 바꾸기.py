import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
busket = [0]*(N+1)
for j in range(1,N+1):
    busket[j] = j 
for i in range(M):
    busket[arr[i][0]], busket[arr[i][1]] =  busket[arr[i][1]],busket[arr[i][0]]
print(*busket[1:])