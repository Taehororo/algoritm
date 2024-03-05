L = 100 # 가로세로 길이 100
l = 10 # 붙이는 색종이의 길이
N = int(input()) # 붙일 종이의 개수
board = [[0] * 101 for _ in range(101)] # 0번 인덱스 안쓸려고 +1 해줌
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0 # 종이를 붙인 검은 영역의 넓이
for paper in arr:
    for i in range(paper[1],paper[1]+10):
        for j in range(paper[0],paper[0]+10):
            board[i][j] = 1

for i in range(L):
    cnt += board[i].count(1)

print(cnt)