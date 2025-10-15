import sys
input = sys.stdin.readline

N = int(input())
R = list(map(int, input().split()))
ans = 0

for i in range(N):
    if i + 2 < N and R[i+1] > R[i+2]:
        # i와 i+1을 (i+1)-(i+2) 만큼 맞춰준다
        take = min(R[i], R[i+1] - R[i+2])
        R[i] -= take
        R[i+1] -= take
        ans += 5 * take

    if i + 2 < N:
        # 가능한 만큼 7원 묶음
        take = min(R[i], R[i+1], R[i+2])
        R[i] -= take
        R[i+1] -= take
        R[i+2] -= take
        ans += 7 * take

    if i + 1 < N:
        # 가능한 만큼 5원 묶음
        take = min(R[i], R[i+1])
        R[i] -= take
        R[i+1] -= take
        ans += 5 * take

    # 남은 것은 싱글
    ans += 3 * R[i]
    R[i] = 0

print(ans)
