import sys
inpurt = sys.stdin.readline
sys.setrecursionlimit(10**6)


N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

M = int(input())
arr2 = list(map(int, input().split()))

N_dict = {}
for n in arr1:
  if n in N_dict:
    N_dict[n] += 1
  else:
    N_dict[n] = 1

for m in arr2:
  if m in N_dict:
    print(N_dict[m], end=' ')
  else:
    print('0', end=' ')