# 14888 연산자 끼워넣기
def dfs(n,sum_val): # 사용한 숫자의 개수,현재 합
    if n == N-1:
        answer.append(sum_val)
        return
    for i in range(4):
        if operator[i] >0:
            if i ==0:
                arr[n]
                operator[i] -= 1
                dfs(n+1,sum_val+arr[n+1])
                operator[i] += 1
            elif i == 1:
                operator[i] -= 1
                dfs(n+1,sum_val-arr[n+1])
                operator[i] += 1
            elif i == 2:
                operator[i] -= 1
                dfs(n+1,sum_val*arr[n+1])
                operator[i] += 1
            elif i == 3:
                operator[i] -= 1
                if sum_val < 0: # 나눠지는 값이 음수일 경우는 특이 처리해줘야함
                    dfs(n+1,-(-sum_val//arr[n+1]))
                else: 
                    dfs(n+1,sum_val//arr[n+1])
                operator[i] += 1
            
    
N = int(input()) # 수의 개수
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))
#         +, -, x, / 의 개수 개수 합은 N-1개임
answer = []
dfs(0,arr[0])
print(max(answer))
print(min(answer))