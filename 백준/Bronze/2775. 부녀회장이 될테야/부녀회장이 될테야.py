import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

for _ in range(T):
    k = int(input()) # 층 수
    n = int(input()) # 호 수
    arr = [[0]*(n+1) for _ in range(k+1)]
    for i in range(1,n+1):
        arr[0][i] = i
    for floor in range(1,k+1):
        arr[floor][1] = arr[floor-1][1]
        for room in range(2,n+1):
            arr[floor][room] = arr[floor][room-1] + arr[floor-1][room]
    print(arr[k][n])