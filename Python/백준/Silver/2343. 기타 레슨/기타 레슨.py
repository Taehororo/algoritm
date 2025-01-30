import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
start = max(arr)
end = sum(arr)
while start <= end:
  mid = (start+end) // 2
  cnt = 1
  sum_cnt = 0
  for i in arr:
    if sum_cnt + i > mid:
      cnt += 1
      sum_cnt = 0
    sum_cnt += i
      
  if cnt <= M:
    answer = mid
    end = mid - 1
  else:
    start = mid + 1
print(answer)