import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N = int(input())
P = list(map(int, input().split()))
P.sort()

time = 0
for i in range(N):
    time += P[i]
    if i == N-1:
        break
    P[i+1] += P[i]
print(time)