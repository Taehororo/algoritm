import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
q = deque([])
for _ in range(N):
    temp = list(input().split())
    if temp[0] =='push':
        q.append(int(temp[1]))
    elif temp[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif temp[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif temp[0] == 'size':
        print(len(q))
    elif temp[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif temp[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)