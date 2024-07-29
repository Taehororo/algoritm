# 2565 전깃줄
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 전깃줄 개수 N
N = int(input())
arr = [list(map(int, input().split())) for  _ in range(N)]
dp = [1]*N

arr.sort(key=lambda x: (x[0], x[1]))
for i in range(1,N):
  for j in range(0,i):
    if arr[j][1] < arr[i][1]:
      dp[i] = max(dp[i], dp[j] +1)

      
print(N- max(dp))