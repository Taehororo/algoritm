# 백준 11722.py 가장 긴 감소하는 부분 수열

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input()) # 수열 A의 크기
A = list(map(int, input().split())) # 수열 A
dp = [1]*N

for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))