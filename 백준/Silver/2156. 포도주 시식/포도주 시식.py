# 백준 2156 포도주 시식
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input()) # 잔의 개수
dp = [[0,0] for _ in range(n+1)]
arr = [0]*(n+1) # 포도주가 있는 잔
for i in range(1,n+1):
    arr[i] = int(input())

# 처음 0인덱스는 0으로 만들어줌
dp[1][0] = arr[1]
dp[1][1] = 1
if n >= 2:
    dp[2][0] = arr[1]+arr[2]
    dp[2][1] = 2


for i in range(3,n+1):
    if dp[i-1][1] == 2: # 이전 잔에서 먹을 수있는 최댓값인데, 그게 연속으로 2잔을 먹었을 경우
        dp[i][0] = max(dp[i-1][0],dp[i-3][0]+arr[i-1]+arr[i],dp[i-2][0]+arr[i])
        if dp[i][0] == dp[i-1][0]: # 요번에 안먹을때가 최대인 경우
            dp[i][1] = 0
        elif dp[i][0] == dp[i-3][0]+arr[i-1]+arr[i]: # 3칸전으로 가고 이전잔과 요번잔을 먹을때가 최대인 경우
            dp[i][1] = 2
        else:   # 2칸전과 요번잔을 먹을 경우
            dp[i][1] = 1
    elif dp[i-1][1] == 1: # 이전 잔에서 먹을 수있는 최댓값인데, 그게 연속으로 1잔을 먹었을 경우
        dp[i][0] = max(dp[i-1][0]+arr[i],dp[i-2][0]+arr[i])
        if dp[i][0] == dp[i-1][0]+arr[i]: 
            dp[i][1] = 2
        else:
            dp[i][1] = 1
    else: # dp[i-1][1] == 0 즉 이전 잔의 술은 먹지 않았을때
        dp[i][0] = dp[i-1][0] + arr[i]
        dp[i][1] = 1

print(max(dp)[0])
