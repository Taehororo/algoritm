import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 누적합 테이블 초기화 (1-index로 사용)
prefix = [[0] * (m+1) for _ in range(n+1)]

# 누적합 계산
for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = (arr[i-1][j-1]
                        + prefix[i-1][j]
                        + prefix[i][j-1]
                        - prefix[i-1][j-1])

# 쿼리 처리
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    result = (prefix[x][y] 
              - prefix[i-1][y] 
              - prefix[x][j-1] 
              + prefix[i-1][j-1])
    print(result)
