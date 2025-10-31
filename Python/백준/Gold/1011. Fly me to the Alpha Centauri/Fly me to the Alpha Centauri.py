t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x  # 전체 거리

    tmp = 0      # 지금까지 이동한 누적 거리
    cnt = 0      # 이동 횟수 (정답)
    move = 1     # 현재 이동할 거리

    # 이동 패턴: 1, 1, 2, 2, 3, 3, ...
    while tmp < distance:
        cnt += 1         # 한 번 이동
        tmp += move      # 현재 이동거리만큼 앞으로 감
        if cnt % 2 == 0: # 두 번 이동할 때마다 이동 거리 1 증가
            move += 1
    print(cnt)