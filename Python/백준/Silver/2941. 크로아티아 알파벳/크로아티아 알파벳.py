import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']

alpha = input().rstrip()
for i in arr:
  alpha = alpha.replace(i,'_')
print(len(alpha))