import sys
sys.setrecursionlimit(10**6)

# 버튼 수
N = int(input())
arr = [0] + list(map(int, input().split()))
# 학생수
M = int(input())

# 남은 1 여는 2 두번째는 누른 스위치 수
student = [list(map(int, input().split())) for _ in range(M)]

for gender, button in student:
  if gender == 1:
    origin = button
    i = 2
    while button <= N: 
      if arr[button]:
        arr[button] = 0
      else:
        arr[button] = 1
      button = origin*i
      i += 1 
  else:
    
    if arr[button]:
      arr[button] = 0
    else:
      arr[button] = 1
    i = 1
    while (1):
      if 1<= (button - i) and (button + i) <= N:
        if arr[button-i] == arr[button +i]:
          if arr[button-i]:
            arr[button-i] = 0
            arr[button +i] = 0
          else:
            arr[button-i] = 1
            arr[button +i] = 1
          i += 1
        else:
          break
      else:
        break


for i in range(1, N+1):
  print(arr[i], end=' ')
  if i % 20 == 0:
    print()