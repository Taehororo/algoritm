# 9935 문자열 폭발
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


arr = list(input().strip())
bomb = list(input().strip())
L = len(bomb)
q = []

for i in arr:
    q.append(i)
    if q[len(q)-L:len(q)] == bomb:
        for _ in range(L):
            q.pop()
if q:
    print(*q, sep='')
else:
    print('FRULA')
