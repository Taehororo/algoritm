# 백준 2193 이친수
import sys
sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
dp = [0]*(N+1)
dp[0] = 0
dp[1] = 1
for i in range(2,N+1):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[N])