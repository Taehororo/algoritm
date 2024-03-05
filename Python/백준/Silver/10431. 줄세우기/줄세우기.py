from collections import deque
import math
P = int(input())
for tc in range(1, P+1):
    arr = list(map(int, input().split()))
    T = arr[0]
    arr = arr[1:]
    key = deque()
    key.append(arr[0])
    cnt = 0
    smallest =0
    for i in range(1,len(arr)):
        if max(key) < arr[i]:
            key.append(arr[i])
            continue
        else:
            smallest = math.inf
            for idx in key:
                if idx > arr[i]:
                    if idx < smallest:
                        smallest = idx
                    else:
                        continue
            temp_idx = key.index(smallest)
            key.append(0)
            for j in range(len(key)-1,temp_idx,-1):
                key[j] = key[j-1]
                cnt += 1
            key[temp_idx] = arr[i]
    print(T,cnt)