# 2293 동전 1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# n가지 종류의 동전, 가치의 합 K
N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
dp = [0]*(K+1)
dp[0] = 1
for coin in arr:
  for i in range(coin, K+1):
    cnt = dp[i-coin]
    dp[i] += cnt
    
print(dp[K])