import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()

answer = 0
for i in range(N):
    value = A[i]
    s = 0
    e = N - 1
    while (s < e):
        if (A[s] + A[e] == value):
            if (s != i and e != i):
                answer += 1
                break
            elif (s == i):
                s += 1
            elif (e == i):
                e -= 1
        elif (A[s] + A[e] < value):
            s += 1
        else:
            e -= 1
            
print(answer)