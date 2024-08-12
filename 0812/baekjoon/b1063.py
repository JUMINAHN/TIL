
# 체스판 만들기
chess = [[0] * 8 for _ in range(8)]
king_p, stone_p, move_count = input().split()

alpha_change_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
king_col, king_row = king_p
king_col = alpha_change_num.get(king_col)
king_row = int(king_row) - 1

stone_col, stone_row = stone_p
stone_col = alpha_change_num.get(stone_col)
stone_row = int(stone_row) - 1

dict = {'R': [0, 1], 'RB': [-1, 1], 'B': [-1, 0], 'LB': [-1, -1], 'L': [0, -1], 'LT': [1, -1], 'T': [1, 0],
        'RT': [1, 1]}
for _ in range(int(move_count)):
    move = input()
    row,col = dict.get(move)
    move_row = int(king_row)+ int(row)
    move_col = king_col + col

    temp_row = int(king_row)
    temp_col = king_col

    if 0 <= move_row < 8 and 0 <= move_col < 8:
        king_row = move_row
        king_col = move_col

        if king_row == stone_row and king_col == stone_col:  # 이동하는 것과 지금 원래있는 돌의 위치들이같다면
            stone_mvrow = int(stone_row) + int(row)
            stone_mvcol = stone_col + col
            if 0 <= stone_mvcol < 8 and 0 <= stone_mvrow < 8:
                stone_row = stone_mvrow
                stone_col = stone_mvcol
            else :
                king_row = temp_row
                king_col = temp_col
    else:
        continue



#숫자를 다시 영어좌표로 바꿔주기
num_change_alpha = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}
king_col = num_change_alpha.get(king_col)
king_row += 1
stone_col = num_change_alpha.get(stone_col)
stone_row += 1
#킹의 위치
print(king_col+str(king_row))

# 돌의 위치
print(stone_col+str(stone_row))