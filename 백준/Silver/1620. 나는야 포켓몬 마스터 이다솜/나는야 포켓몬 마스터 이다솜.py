import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split()) # 포켓몬 개수 N, 문제 개수 M
# arr = [[0] for _ in range(N+1)]
dict1 = {} # 포켓몬으로 저장
dict2 = {} # 번호로 저장
for i in range(N):
    poketmon = input().rstrip()
    dict1[poketmon] = i+1
    dict2[i+1] = poketmon

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(dict2[int(question)])
    else:
        print(dict1[question])

# 배열로 하니 시간초과 걸림
# for i in range(N):
#     poketmon = input().rstrip()
#     arr[i+1] = poketmon
# for _ in range(M):
#     question = input().rstrip()
#     if question.isdigit():
#         print(arr[int(question)])
#     else:
#         print(arr.index(question))
