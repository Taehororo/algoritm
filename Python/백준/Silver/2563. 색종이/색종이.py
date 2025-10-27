import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())

# y x 순서임
answer = [[0]*101 for _ in range(101)]
arr =[list(map(int, input().split())) for _ in range(N)]
cnt = 0
for y, x in arr:
  for i in range(x, x+10):
    if 0 <= i < 101:
      for j in range(y, y+10):
        if 0 <= j < 101:
          if answer[i][j] == 0:
            answer[i][j] = 1
            cnt += 1
print(cnt)