import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(arr)
sort_arr_dict = {}
tmp = 0
for x in sort_arr:
  if x in sort_arr_dict:
    pass
  else:
    sort_arr_dict[x] = tmp
    tmp += 1

for x in arr:
  print(sort_arr_dict[x], end=' ')

