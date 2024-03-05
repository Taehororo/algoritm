H, W = map(int,input().split())
arr = [input() for _ in range(H)] # 입력으로 받는 지도정보
matrix = [[-1]*W for _ in range(H)] # 구름이 언제 도착하는지 저장할지도정보
for i in range(H):  
    if 'c' in arr[i]: # 일단 초기에 구름이 있는 위치에 0을 할당한다.
        for j in range(W):
            if arr[i][j] == 'c':
                matrix[i][j] = 0
    else:
        continue

for i in range(H):
    if 0 in matrix[i]: # 구름이 행에 있을때 반복시작
        for j in range(W):
            if matrix[i][j] == 0: # 구름이 있을때?
                cnt = 0 # 구름이 도착하는데 걸리는 시간
                while True:
                    j += 1 # 오른쪽으로 한칸이동
                    cnt += 1 # 구름이 도착하는데 걸리는 시간
                    try:
                        if matrix[i][j] == -1 or matrix[i][j] > cnt: 
                            # -1로 되있거나, 
                            # 기존에 구름이 도착하는데 걸리는 시간이 더 길다면
                            # 도착하는데 걸리는 시간 갱신
                            matrix[i][j] = cnt
                    except: # 범위밖으로 나가버리면 반복 끝내기
                        break
for i in range(H):
    print(*matrix[i]) #출력하기