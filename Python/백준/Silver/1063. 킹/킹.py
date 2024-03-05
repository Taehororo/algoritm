move_dict = {
    'R' : (0,1),
    'L' : (0,-1),
    'B' : (1,0),
    'T' : (-1,0),
    'RT': (-1,1),
    'LT': (-1,-1),
    'RB': (1,1),
    'LB': (1,-1)
}
check_alpha = ['A','B','C','D','E','F','G','H']
check_num = ['8','7','6','5','4','3','2','1']
matrix = [[0]*8 for _ in range(8)] # 체스판

king_pos, stone_pos, N = map(str,input().split())
move_list = [input() for _ in range(int(N))]
# 왕의 위치는 1로
# 돌의 위치는 2로
k_pos_i = check_num.index(king_pos[1])
k_pos_j = check_alpha.index(king_pos[0])
matrix[k_pos_i][k_pos_j] = 1
stone_pos_i = check_num.index(stone_pos[1])
stone_pos_j = check_alpha.index(stone_pos[0])
matrix[stone_pos_i][stone_pos_j] = 2

for move in move_list:
    direct = move_dict[move]
    dx, dy = direct[0], direct[1]
    if 0 <= k_pos_i+dx <= 7 and 0 <= k_pos_j+dy <= 7:
        if matrix[k_pos_i+dx][k_pos_j+dy] == 2: #돌을쳤을때
            if 0 <=stone_pos_i+dx <= 7 and 0<= stone_pos_j+dy <= 7:
                # 체스판안에있을때
                matrix[stone_pos_i + dx][stone_pos_j + dy] = 2
                matrix[stone_pos_i][stone_pos_j] = 1
                stone_pos_i += dx
                stone_pos_j += dy
                matrix[k_pos_i][k_pos_j] = 0
                k_pos_i += dx
                k_pos_j += dy
        else:
            matrix[k_pos_i][k_pos_j] = 0
            k_pos_i += dx
            k_pos_j += dy
            matrix[k_pos_i][k_pos_j] = 1
    else:
        continue
print(f'{check_alpha[k_pos_j]}{check_num[k_pos_i]}')
print(f'{check_alpha[stone_pos_j]}{check_num[stone_pos_i]}')