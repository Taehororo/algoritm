import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

# 오른쪽으로만 진행: ↗, →, ↘ (이 순서가 그리디하게 최적)
dirs = (-1, 0, 1)

def dfs(r, c):
    arr[r][c] = 'x'          # 현재 칸을 사용 처리 (되돌리지 않음: 가지치기)
    if c == C - 1:
        return True
    for dr in dirs:
        nr, nc = r + dr, c + 1
        if 0 <= nr < R and nc < C and arr[nr][nc] == '.':
            if dfs(nr, nc):
                return True
    return False

ans = 0
for i in range(R):
    # 문제에서 첫/마지막 열은 항상 비어있다고 하지만, 안전하게 체크
    if arr[i][0] == '.' and dfs(i, 0):
        ans += 1

print(ans)
