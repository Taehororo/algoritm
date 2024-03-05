# 2667 단지번호 붙이기
from pprint import pprint
def find_path(x,y):
    global house_cnt
    visited.append((x,y))
    #               위     아래    오른쪽   왼쪽
    for dx,dy in ((-1,0), (1,0), (0, 1), (0, -1)):
        if 0<= x+dx< N and 0<= y+dy < N: # 범위 안에 있을때
            if (x+dx, y+dy) not in visited and arr[x+dx][y+dy] == '1':
                house_cnt += 1 # 단지 내 집의 개수를 세는 변수
                find_path(x+dx,y+dy)

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = []
house = []
cnt = 0 # 그룹의 횟수
for i in range(N):
    for j in range(N):
        # 1이고 여태까지 방문하지 않았던 곳이라면
        if arr[i][j] == '1' and (i,j) not in visited:
            house_cnt = 1 # 단지내 집의 개수 시작하는 곳의 위치도 포함시켜야하기에 1개부터시작
            # 함수 실행 , 연결되어있는 모든 1을 갔다오면 방문처리를 해준다.
            find_path(i,j)
            house.append(house_cnt) # 단지내 집의 개수
            cnt += 1  # 그룹의 횟수 증가

print(cnt) # 단지의 개수
house.sort() # 단지내 집의개수 정렬
for i in house:
    print(i) # 단지내 집의 개수