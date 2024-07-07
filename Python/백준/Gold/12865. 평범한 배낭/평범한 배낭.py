# 12865 평범한 배낭
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 물품의 수 N, 버틸수 있는 무게 K
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K+1) for _ in range(N+1) ]

for i in range(1, N+1):
  for j in range(1, K+1):
    weight = arr[i-1][0]
    value = arr[i-1][1]
    if j < weight:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])

print(dp[-1][-1])
      

