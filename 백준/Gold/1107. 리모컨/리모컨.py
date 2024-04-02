# 1107 리모컨
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N =int(input()) # 이동할 채널 번호
M = int(input()) # 고장난 버튼 개수
arr = list(map(int, input().split())) # 고장난 버튼

count = abs(100 - N)

for num in range(1000000):
    num = str(num)   
    for j in range(len(num)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(num[j]) in arr:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(num) - 1:
            count = min(count, abs(int(num) - N) + len(num))

print(count)