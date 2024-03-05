T = int(input())
def start():
    sold_bread = 0
    for person in customers:
        # 공식, 특정시간에 만들 수 있는 빵의 개수
        made_bread = (person// m)* k
        # 빵을 1개 팔았따
        sold_bread += 1
        # 재고 계산
        remain = made_bread - sold_bread
  
        # 재고가 0보다 작으면 실패
        if remain < 0:
            return 'Impossible'
        # 실패가 없었으면 성고
    return 'Possible'
for tc in range(1, T+1):
    n,m,k = map(int, input().split())
    customers = list(map(int, input().split()))
    customers.sort()
    result = start()
    print(f'#{tc} {result}')
