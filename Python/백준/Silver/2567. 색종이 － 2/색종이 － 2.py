# 2567. 색종이 -2
L = 101 # 가로세로 길이 100
l = 10 # 붙이는 색종이의 길이
N = int(input()) # 붙일 종이의 개수
board = [[0] * L for _ in range(L)] # 0번 인덱스 안쓸려고 +1 해줌
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0 # 검은 영역의 테두리
for paper in arr:
    for i in range(paper[1],paper[1]+10):
        for j in range(paper[0],paper[0]+10):
            board[i][j] = 1


for i in range(L):
    for j in range(L):
        if board[i][j] == 1:  # 1 즉 색종이가 붙어있는 영역에서 4방향으로 델타 담색
            # 8 6 2 4
            for dx,dy in ((-1,0),(0,1),(1,0),(0,-1)): # 만약 0이 있다면 경계,즉 둘레에 있다는 뜻
                mx = i + dx
                my = j + dy
                if mx < 0 or mx > L or my < 0 or my > L:
                    cnt += 1
                    continue
                if board[mx][my] == 0:
                    cnt += 1
print(cnt)