import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
A, B = map(int, input().split())
arr_A = sorted(list(map(int, input().split())))
arr_B = sorted(list(map(int, input().split())))
b_dict = {}
cnt = 0
ans = []
for b in arr_B:
  b_dict[b]= b

for a in arr_A:
  try:
    if b_dict[a]:
      pass
  except:
    cnt += 1
    ans.append(a)
print(cnt)
for an in ans:
  print(an, end=' ')
