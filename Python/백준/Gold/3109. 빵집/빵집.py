import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
ans = 0
drs = (-1,0,1)


def dfs(r,c):
  arr[r][c] = 'x'
  if c == C-1:
    return True
  
  for dr in drs:
    nr, nc = r + dr , c +1
    if 0 <= nr < R and nc < C and arr[nr][nc] == '.':
      if dfs(nr,nc):
        return True
  return False
      

for i in range(R):
  if dfs(i,0):
    ans += 1

print(ans)