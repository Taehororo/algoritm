L = int(input())
N = int(input())
arr =[list(map(int, input().split())) for _ in range(N)]
customer = [0]*(L+1)
an1 = arr.index(max(arr, key=lambda x: x[1]-x[0]))+1
an2 = 0
number = 1
for i in range(N):
    p, k = arr[i][0],arr[i][1]
    for idx in range(p-1,k):
        try:
            if customer[idx] == 0:
                customer[idx] = number
        except:
            break
    number += 1
an2 = 0
temp_ans=0
for j in range(1,N+1):
    temp = customer.count(j)
    if temp > temp_ans:
        an2 = j
        temp_ans = temp
print(an1)
print(an2)