import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
start, end = 1, trees[-1]
ans = 0
if N == 1:
  ans = trees[0] - M
else:
  while start <= end:
    mid = (start + end) // 2
    cnt = 0 
    for tree in trees:
      if tree > mid:
        cnt += tree - mid
    if cnt >= M:
      if ans >= mid:
        break
      start = mid + 1
      ans = mid
    else:
      end = mid - 1
print(ans)