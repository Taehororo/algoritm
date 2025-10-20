import sys
input = sys.stdin.readline

n, c = map(int, input().split())  # 마을 수, 트럭 용량
m = int(input())  # 배송 요청 수

boxes = [list(map(int, input().split())) for _ in range(m)]
boxes.sort(key=lambda x: (x[1], x[0]))  # 도착 마을 기준 정렬

capacity = [c] * (n + 1)  # 각 구간별 남은 용량
answer = 0

for s, e, b in boxes:
    # s부터 e-1까지 중 최소 남은 용량 구함
    possible = min(capacity[s:e])
    # 실을 수 있는 실제 박스 수
    take = min(possible, b)
    # 그만큼 용량 감소
    for i in range(s, e):
        capacity[i] -= take
    answer += take

print(answer)