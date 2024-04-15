# 1912 연속합
import sys
sys.setrecursionlimit(10**6)
input= sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = arr.copy()

for i in range(1,n):
    dp[i]=max(dp[i],dp[i-1]+arr[i])
print(max(dp))