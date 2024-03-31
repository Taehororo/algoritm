import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
arr = [0]*(10001)
for _ in range(N):
	idx= int(input())
	arr[idx] += 1

n_cnt = 0
for i in range(10001):
	if n_cnt == N:
		break
	if arr[i] > 0:
		while arr[i] >0:
			print(i)
			arr[i] -= 1
		n_cnt +=1