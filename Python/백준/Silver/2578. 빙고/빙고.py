N = 5 # 빙코판 크기
arr = [list(map(int, input().split())) for _ in range(N)]
answer = [list(map(int, input().split())) for _ in range(N)]

cnt = 0 # 사회자가 숫자를 부른 회숫

for i in range(N):
    for j in range(N):
        cnt += 1
        ans = answer[i][j]
        for z in range(N):
            if ans in arr[z]:
                arr[z][arr[z].index(ans)] = 0
                # 8,9,6,3
                bbingo = 0
                for x in range(N):
                    for y in range(N):
                        if arr[x][y] == 0:
                            for dx,dy in ((-1,0),(-1,1),(0,1),(1,1)):
                                for mul in range(1,5):
                                    mx = x + dx*mul
                                    my = y + dy*mul
                                    if 0 <= mx < 5 and 0<= my < 5 and arr[mx][my] == 0:
                                        continue
                                    else:
                                        break
                                else: # 위에서 정상적으로 for문을 다돌린경우 즉 빙고가 있는경우
                                    bbingo += 1
                                    if bbingo == 3: # 빙고 3줄 완성시
                                        print(cnt)
                                        quit()