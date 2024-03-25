# 1043 거짓말
N, M = map(int, input().split())
# 사람의 수 N과 파티의 수 M

lies = list(map(int, input().split()))
party = [[] for _ in range(M)]
true = [] # 진실을 알고 있는 사람을 넣을 배열

for i in range(M):
    party[i] = list(map(int,input().split()))

visited = [0]*(N+1)
if lies[0] == 0: # 진실을 알고있는 사람이 없을 경우
    print(M)
else:
    true_people = lies[1:] 
    for t in true_people:
        true.append(t)
        visited[t] = 1
    
    i = 0

    count = 0
    while True: # 진실을 알고있는 사람이 속해있는 파티의 사람은 진실에 넣어줘야한다.    
        temp = party[i][1:]
        flag = False
        for people in temp:
            if people in true:
                flag = True
            
        if flag:
            for people in temp:
                if people not in true:
                    true.append(people)       
        i += 1
        if i == M:
            count += 1
            i = 0
        if count == M:
            break
                         
    cnt = 0 # 과장된 말을 할수 잇는 횟수
    for i in range(M):
        temp = party[i][1:]
        for people in temp:
            if people in true:
                
                break
        else:
            cnt += 1

    print(cnt)