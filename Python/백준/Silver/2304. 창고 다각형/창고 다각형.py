N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
top_h = max(arr,key=lambda x: x[1])[1] # 가장 높은 기둥
h = arr[0][1] # 현재 지붕의 높이
h_idx = arr[0][0] # 현재 지붕이 시작한 위치
cnt = 0 # 면적

for i in range(N):

    if h < arr[i][1] < top_h:
        cnt += (arr[i][0] - h_idx)*h
        h_idx = arr[i][0]
        h = arr[i][1]
    if arr[i][1] == top_h:
        cnt += (arr[i][0] - h_idx)*h
        cnt += top_h
        if i + 1 == N:
            break
        h_idx = arr[i][0]+1
        h = max(arr[i+1:], key=lambda x: x[1])[1]
        top_h = max(arr[i+1:], key=lambda x: x[1])[1]


print(cnt)