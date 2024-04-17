# 백준 14501 퇴사
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
arr = [[0,0] for _ in range(N)]
dp = [0]*(N+1)
for i in range(N):
    T, P = map(int, input().split())
    arr[i][0] = T
    arr[i][1] = P
for i in range(N):
    for j in range(i+arr[i][0], N+1):
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]
print(dp[N])