# 2579.py 계단 오르기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input()) # 계단의 수
arr = [0]*(N+1) # 각 계단의 점수
dp = [[0,0] for _ in range(N+1)]

for i in range(1,N+1):
    arr[i] = int(input())
dp[1][0] = arr[1]
dp[1][1] = 1
for i in range(2,N+1):
    
    if dp[i-1][1] == 1:
        if dp[i-1][0]+arr[i] > dp[i-2][0]+arr[i]:
            dp[i][0] = dp[i-1][0]+arr[i]
            dp[i][1] = 2
        else:
            dp[i][0] = dp[i-2][0]+arr[i]
            dp[i][1] = 1
            
    elif dp[i-1][1] == 2:
        if dp[i-3][0]+arr[i-1]+arr[i] > dp[i-2][0] + arr[i]:
            dp[i][0] = dp[i-3][0]+arr[i-1]+arr[i]
            dp[i][1] = 2
        else:
            dp[i][0] = dp[i-2][0] + arr[i]
            dp[i][1] = 1

print(dp[N][0])