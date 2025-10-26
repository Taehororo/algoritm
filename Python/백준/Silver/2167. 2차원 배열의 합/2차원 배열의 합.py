import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = [[0]*(M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
K = int(input())
arr2 = [list(map(int, input().split())) for _ in range(K)]

ans = []

for i,j,x,y in arr2:
  cnt = 0
  for t in range(i,x+1):
    cnt += sum(arr[t][j:y+1])
  print(cnt)
