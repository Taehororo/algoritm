# 백준 9461 파도반 수열 날먹문제
#  P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T1_faker = int(input())

for _ in range(T1_faker):
    N = int(input())
    if N <= 3:
        print(1)
    else:
        arr = [0]*(N+1)
        arr[1] = 1
        arr[2] = 1
        arr[3] = 1
        for i in range(4,N+1):
            arr[i] = arr[i-3]+arr[i-2]
        print(arr[N])
