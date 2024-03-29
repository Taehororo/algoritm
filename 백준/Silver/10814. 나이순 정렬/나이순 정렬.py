# 10814 나이순 정렬
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    age, name = input().split()
    arr[i]=[int(age),name]

arr.sort(key=lambda x:x[0])
# 그냥 sort하면 앞에것도 오른차순,뒤에것도 오름차순인데
# key를 통해 sort하면 앞에것만 오름차순으로 정렬된다.

for i in range(N):
    print(*arr[i],)
