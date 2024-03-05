N = int(input())
board = [list((input())) for _ in range(N)]
di = [0, 0, 1, 0, -1]
dj = [0, 1, 0, -1, 0]
result = []
max_result = 0
for i in range(N):
    for j in range(N):
        for k in range(5):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                board[ni][nj], board[i][j] = board[i][j], board[ni][nj]
                max_cnt = 0
                for r in range(N):
                    cnt = 0
                    for c in range(N):
                        if c + 1 < N and board[r][c] == board[r][c + 1]:
                            cnt += 1
                            if cnt > max_cnt:
                                max_cnt = cnt
                        else:
                            cnt = 0
                result.append(max_cnt + 1)

                max_cnt = 0
                for c in range(N):
                    cnt = 0
                    for r in range(N):
                        if r + 1 < N and board[r][c] == board[r + 1][c]:
                            cnt += 1
                            if cnt > max_cnt:
                                max_cnt = cnt
                        else:
                            cnt = 0
                result.append(max_cnt + 1)
                if max_result < max(result):
                    max_result = max(result)
                result = []
                board[ni][nj], board[i][j] = board[i][j], board[ni][nj]

print(max_result)