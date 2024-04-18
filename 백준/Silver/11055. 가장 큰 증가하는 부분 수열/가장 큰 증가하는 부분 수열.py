# 백준 11055 가장 큰 증가하는 부분 수열
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int, input().split()))
dp = [0]*N
dp[0] = A[0]


for i in range(1,N):
    temp = i-1
    flag = True
    while temp >= 0:
        if A[i] > A[temp]:
            dp[i]= max(dp[i], dp[temp] + A[i])
        temp -= 1
    dp[i] = max(dp[i],A[i])        
print(max(dp))