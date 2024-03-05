from itertools import combinations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
comb = combinations(arr, 3)
comb = list(comb)
max_val = 0
for i in range(len(comb)):
    temp_sum = comb[i][0]+comb[i][1]+comb[i][2]
    if temp_sum <= M:
        max_val = max(temp_sum, max_val)
print(max_val)
