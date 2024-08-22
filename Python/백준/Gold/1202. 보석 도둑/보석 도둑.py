import sys
from heapq import heappush, heappop
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
gems.sort()
bags.sort()
sumValue = 0
maxheap = []

for bag in bags:
  while gems and gems[0][0] <= bag:
    heappush(maxheap, -gems[0][1])
    heappop(gems)
  if maxheap:
    sumValue -= heappop(maxheap)
print(sumValue)
