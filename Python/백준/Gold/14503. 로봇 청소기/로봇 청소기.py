import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방향: 0=북,1=동,2=남,3=서
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ans = 0

while True:
    # 1) 현재 칸 청소
    if arr[r][c] == 0:
        arr[r][c] = 2
        ans += 1

    # 2) 왼쪽으로 회전하며 청소할 곳 찾기 (최대 4번)
    moved = False
    for _ in range(4):
        # 왼쪽으로 회전
        d = (d + 3) % 4  # 왼쪽은 -1, 모듈로 처리
        nr = r + dirs[d][0]
        nc = c + dirs[d][1]
        # 범위 확인 및 아직 청소 안된 칸(0)인지 확인
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            # 방향을 바꾼 상태에서 전진
            r, c = nr, nc
            moved = True
            break

    if moved:
        # 새 칸에서 다시 루프 시작 (청소는 루프에서 처리)
        continue

    # 3) 네 방향 모두 청소되어 있거나 벽인 경우: 후진 시도
    back_dir = (d + 2) % 4
    br = r + dirs[back_dir][0]
    bc = c + dirs[back_dir][1]
    # 후진할 수 없으면 종료
    if not (0 <= br < N and 0 <= bc < M) or arr[br][bc] == 1:
        break
    # 후진 (방향은 바뀌지 않음)
    r, c = br, bc

print(ans)
