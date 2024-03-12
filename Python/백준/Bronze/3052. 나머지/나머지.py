import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(10)]
for i in range(10):
    arr[i] = arr[i]%42
print(len(set(arr)))