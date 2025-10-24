import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()
arr = []
for i in range (N-1):
  arr.append(abs(sensor[i]-sensor[i+1]))

arr.sort(reverse=True)

if K >= N:
  print(0)
else:
  print(sum(arr[K-1:]))

