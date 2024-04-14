# 11053.py 가장 긴 증가하는 부분 수열
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))
dp=[1]*N 
for i in range(1,N):
    for j in range(i):
        if arr[i]>arr[j]: 
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))