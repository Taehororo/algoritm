# 백준 11054 가장 긴 바이토닉 부분 수열
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n=int(input())
arr= list(map(int,input().split()))
dp1=[1]*1000
dp2=[1]*1000

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp1[i]=max(dp1[j]+1,dp1[i])

for i in range(n-1,-1,-1):
    for j in range(i,-1,-1):
        if arr[i]<arr[j]:
            dp2[j]=max(dp2[i]+1,dp2[j])

result=[0 for i in range(n)]
for i in range(n):
    result[i] =dp1[i]+dp2[i]-1
print(max(result))