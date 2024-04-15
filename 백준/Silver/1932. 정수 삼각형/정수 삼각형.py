import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n)]
dp = [[] for _ in range(n)]
for i in range(n):
    dp[i] = [0]*(i+1)
for i in range(n):
    arr[i] = list(map(int, input().split()))
dp[0] = arr[0]

for i in range(1,n):
    dp[i][0] = dp[i-1][0] + arr[i][0] # 맨왼쪽
    dp[i][i] = dp[i-1][i-1] + arr[i][i] # 맨오른쪽
    for j in range(1,i): # 가운데 애들
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+arr[i][j]
print(max(dp[i]))