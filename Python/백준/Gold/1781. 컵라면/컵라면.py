import sys
import heapq
input = sys.stdin.readline
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

heap = []
for d, k in arr:
  heapq.heappush(heap,k)
  if len(heap) > d:
    heapq.heappop(heap)
  
print(sum(heap))