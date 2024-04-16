# 1010 다리 놓기
import sys
from itertools import combinations
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T1_faker = int(input())

def dp_factorial(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        dp[i] = dp[i-1] * i
    return dp

for tc in range(T1_faker):
    N, M = map(int, input().split())
    # 시간초과 엔딩
    # arr = [i for i in range(M)]
    # print(len(list(combinations(arr,N))))

    # factorial 함수를 dp로 만들어서 한다.
    # nCr = n! // (r! * (n-r)! ) 함수를 재현한것이다.
    fact_arr = dp_factorial(M)
    n = fact_arr[M]
    r = fact_arr[N]
    n_r = fact_arr[M-N]
    print(n//(r*n_r))