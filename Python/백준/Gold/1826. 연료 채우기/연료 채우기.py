import sys
sys.setrecursionlimit(10**6)
from heapq import heappop,heappush

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
L, P = map(int, input().split())
arr.sort()

ans = 0
car_oil = P
gas_statioin = []

if P >= L:
  print(0)
else:
  for a, b in arr:
    if a > car_oil:
      while gas_statioin and car_oil < a:
        car_oil -= heappop(gas_statioin)
        ans += 1
      # 도착못할경우     
      if a > car_oil:
        if not gas_statioin:
          ans = -1
          break
      else:
        heappush(gas_statioin, -b)
    else:
      heappush(gas_statioin, -b)
  
  if L > car_oil:
    while gas_statioin and car_oil < L:
        car_oil -= heappop(gas_statioin)
        ans += 1
      # 도착못할경우
    if L > car_oil and not gas_statioin:
      ans = -1

  print(ans)