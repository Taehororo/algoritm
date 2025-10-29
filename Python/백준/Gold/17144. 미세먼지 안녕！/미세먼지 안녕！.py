import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#미세먼지 확산시키는 함수
def spread():  
    v=[[0]*C for _ in range(R)]
    
    #4방향 검사 후 v배열에 값들을 저장해둔다.
    for i in range(R):
       for j in range(C):
            if arr[i][j] != 0 and arr[i][j] != -1:
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    
                    if 0<=nx<R and 0<=ny<C and arr[nx][ny] != -1:
                        mungi = arr[i][j] // 5
                        v[nx][ny] += mungi
                        v[i][j] -= mungi
    
    #위의 검사가 끝나고난 후 arr에 v배열 값들을 합침
    for i in range(R):
        for j in range(C):
            arr[i][j]+=v[i][j]

#공기청정기 위에부분 청소
def clean_up():
    #동쪽부터시작하니 d=0
    d=0
    before=0
    #로봇의 시작부분 다음칸부터 시작
    x, y = machine[0][0],machine[0][1]+1
    
    #로봇이 공기청정기를 만나거나 벽을만나면 방향을 꺾는 조건문 추가
    while True:
        nx = x+dx[d]
        ny = y+dy[d]
        
        if nx == R or ny == C or nx == -1 or ny == -1:
            d = (d-1)%4
            continue
        
        if x == machine[0][0] and y == machine[0][1]:
            break
        
        arr[x][y], before = before, arr[x][y]
        x,y = nx,ny

#공기청정기 아래부분 청소
def clean_down():
    #동쪽부터시작하니 d=0
    d=0
    before=0
    
    #로봇의 시작부분 다음칸부터 시작
    x,y = machine[1][0],machine[1][1]+1
    
    #로봇이 공기청정기를 만나거나 벽을만나면 방향을 꺾는 조건문 추가
    while True:
        nx = x+dx[d]
        ny = y+dy[d]
        
        if nx == R or ny == C or nx == -1 or ny == -1:
            d = (d+1)%4
            continue
            
        if x == machine[1][0] and y ==machine[1][1]:
            break
        
        arr[x][y],before = before,arr[x][y]
        x,y=nx,ny

if __name__=='__main__':
    R,C,T = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]
    
    #로봇의 위치 저장하는 배열
    machine=[]
    
    #미세먼지 누적 합 저장
    result=0
    
    #동남서북 4방향
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    
    #로봇의 위치찾아서 machine 배열에 저장
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                machine.append((i,j))
                
    
    #입력받은 T만큼 반복
    for _ in range(T):
        spread()
        clean_up()
        clean_down()
    
    #미세먼지의 양을 찾아서 result에 누적함
    for i in range(R):
        for j in range(C):
            if arr[i][j] != 0 and arr[i][j] != -1:
                result += arr[i][j]
    
    print(result)