import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

start, end = 0, len(liquid) - 1
ans_liquid = 2000000001
ans_a = start
ans_b = end

if len(liquid) == 2:
  print(liquid[ans_a], liquid[ans_b])
else:
  while start < end:
    mid = (start + end) // 2
    sum_liquid = liquid[start] + liquid[end]
    if ans_liquid > abs(sum_liquid):
      ans_liquid = abs(sum_liquid)
      ans_a = start
      ans_b = end
      
    if sum_liquid > 0:
      end -= 1
    elif sum_liquid < 0:
      start += 1
    else:
      break
  print(liquid[ans_a], liquid[ans_b])

