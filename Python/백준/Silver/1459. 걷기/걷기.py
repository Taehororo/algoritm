import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# x좌표,y좌표, 직선,대각
X, Y, W, S = map(int, input().split())

cross = True
cnt = 0

if 2*W < S:
  cross = False

if cross:
  cnt += min(X,Y)*S
  if W > S:
    if abs(X-Y) % 2 == 0:
      cnt += abs(X-Y)*S
    else:
      
      temp = abs(X-Y)%2
      cnt += (abs(X-Y)-temp)*S
      cnt += (temp)*W 
  else:
    cnt += abs(X-Y)*W
else:
  cnt += min(X,Y)*2*W
  cnt += abs(X-Y)*W
print(cnt)