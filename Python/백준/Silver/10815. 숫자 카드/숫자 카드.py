import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
N_arr = list(map(int, input().split()))
N_dict = {}
M = int(input())
M_arr = list(map(int, input().split()))
for n in N_arr:
  N_dict[n] = 1
for m in M_arr:
  if m in N_dict:
    print(1, end=' ')
  else:
    print(0, end=' ')
