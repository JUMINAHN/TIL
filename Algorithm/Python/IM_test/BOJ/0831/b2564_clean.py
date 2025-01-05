#달팽이 접근

import copy


def find_start(direct, distance):
    row = 0
    col = 0
    if direct == 1:
        row = 0
        col = distance
    elif direct == 2:
        row = R
        col = distance
    elif direct == 3:
        row = distance
        col = 0
    else:  # 4
        row = distance
        col = C
    return (row,col)

def min_block(r, c, block):
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]
    data_row2 = [0, -1, 0, 1] #이거까지 바꿔준다
    data_col2 = [-1, 0, 1, 0]

    total_distance = 0
    for i in range(1, store_count + 1): #1에
        right_first = block_loop(data_row, data_col, r, c, block, i) #cout개수를 전달받고
        left_first = block_loop(data_row2, data_col2, r, c, block, i)
        if right_first < left_first:
            total_distance += right_first
        else :
            total_distance += left_first
    return total_distance

def block_loop(data_row, data_col, r, c, block, i):

    row = r
    col = c
    k = 0  # 방향
    count = 0
    block2 = copy.deepcopy(block)

    while count <= (C + R) * 2:
        if block[row][col] == i:
            break
        block2[row][col] = '#'
        move_row = row + data_row[k]
        move_col = col + data_col[k]
        if 0 <= move_row <= R and 0 <= move_col <= C and block2[move_row][move_col] != '#':
            row = move_row
            col = move_col
            count += 1  # 1칸 전진 카운트
        else:
            k = (k + 1) % 4
    return count

C,R = map(int, input().split())
block = [['#']*(C+1) for _ in range(R+1)]
for row in range(R+1):
    for col in range(C+1):
        if row == 0 or col == 0 or row == R or col == C:
            block[row][col] = 0

store_count = int(input())
for i in range(1, store_count+1):
    direct, distance = map(int, input().split())
    if direct == 1:
        block[0][distance] = i
    elif direct == 2:
        block[R][distance] = i
    elif direct == 3:
        block[distance][0] = i
    else :
        block[distance][C] = i
direct, distance = map(int, input().split())
row, col = find_start(direct, distance)


result = min_block(row,col,block)
print(result)