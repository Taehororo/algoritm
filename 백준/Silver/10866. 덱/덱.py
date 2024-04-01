# 10866 덱
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(str, input().split()))
q = deque([])
for i in range(N):
    if arr[i][0] =='push_back':
        q.append(int(arr[i][1]))
    elif arr[i][0] == 'push_front':
        q.appendleft(int(arr[i][1]))
    elif arr[i][0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif arr[i][0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif arr[i][0] == 'size':
        print(len(q))
    elif arr[i][0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif arr[i][0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif arr[i][0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)