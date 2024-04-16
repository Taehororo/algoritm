# 백준 2748 피보나치 수2
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
L = len(arr)

n = int(input())

if n <= L-1:
    print(arr[n])
else:
    for i in range(18,n+1):
        arr.append(arr[i-2]+arr[i-1])
    print(arr[n])