# 1182. 부분수열의 합
from itertools import combinations
import sys
input = sys.stdin.readline

N, S = map(int, input().split()) # 정수의 개수 N 목표값 S
arr = list(map(int, input().split()))

cnt = 0 # 합이 S인 개수
for i in range(1,N+1):# 1부터 시작, 공집합은 뺌
    temp = combinations(arr,i) # 1~N 개까지 부분집합 만들고
    for item in temp: # 이 부분집합 개수 중에 
        if sum(item) == S: # 합이 S인게 있다면
            cnt += 1 # 개수 증가
print(cnt)