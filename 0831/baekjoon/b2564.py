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
    # 문제는 여기임 for문에서 다돌아버리니까 문제가 발생했음 -> 따라서 또 나눠준다.
    # 상점 만큼 돌아야 하기 때문에
    # #순회 방향을 오른쪽으로 기준할 때
    data_row = [0, 1, 0, -1]  # 올라가면(위) ㄱㅊ, 내려가면?
    data_col = [1, 0, -1, 0]
    # 순회 방향을 왼쪽으로 기준할 떄
    data_row2 = [0, 1, 0, -1]
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

def block_loop(data_row, data_col, r, c, block, i): #상점 번호까지 받아야 함
    # row,count 여기서 초기화 값을 계속 유지해야할 듯 --> 추가하기
    row = r
    col = c
    k = 0  # 방향
    count = 0  # 첫번째 count를 해줌 -> 이동하면 count를 하는 것으로 바꿔줌
    #.copy는 얕은 복사.. : 이게 문제였따.. -> 깊은복사 deepcopy
    block2 = copy.deepcopy(block)# 계속 새로운것 copy하고 리셋해줌
    # 순회 방향을 오른쪽으로 기준할 때 -> 지금 배열 자체를 쓰지말고 copy로 똑같은 것을 하나 더 만들어서 count해야할 듯
    while count <= (C + R) * 2:  # 정사각형 만큼이니까.
        # 만약 모두 순회하기 전에 내가 원하는 것을 만난다면
        #왔던길을 막지 않았음
        if block[row][col] == i: #위치의 문제
            break  # while문 break
        block2[row][col] = '#'
        move_row = row + data_row[k]
        move_col = col + data_col[k]
        #이 숫자여야한다가 문제가 되는 것
        #오른쪽으로 안가.. : 그 이유는 R만큼 갈 수 있는데 내가 범위설정을 잘못함 여기선 가능
        if 0 <= move_row <= R and 0 <= move_col <= C and block2[move_row][move_col] != '#':  # 숫자여야 하고, 오타발생
            row = move_row
            col = move_col
            count += 1  # 1칸 전진 카운트
        else:
            k = (k + 1) % 4
    # if total_count == 0:
    #     total_count = count
    # elif total_count > count:
    #     total_count = count
    return count

C,R = map(int, input().split()) #열, 행
#블록을 세알렸을떄 1개 더 있어야함 0부터 10까지 모두 들어가기 때문에 -> 선을 기준ㅇ르ㅗ
block = [['#']*(C+1) for _ in range(R+1)]#block만큼 빈배열 만들기 -> 문자를 넣었음, 숫자에만 접근할 수 있도록
for row in range(R+1):
    for col in range(C+1):
        if row == 0 or col == 0 or row == R or col == C:
            block[row][col] = 0 #을 넣겠습니다.
# print(block) #블록에 맞게 들어갔는지 확인 -> 사방이 맞게 둘려쌓여있음

store_count = int(input()) #상점의 개수
for i in range(1, store_count+1): #상점의 개수를 배열안에 넣기 위해서
    direct, distance = map(int, input().split())
    if direct == 1: #row가 0, col이 distance
        block[0][distance] = i #상점의 값
    elif direct == 2: #row가 R, col이 distance
        block[R][distance] = i
    elif direct == 3: #col이 0, row가 distance
        block[distance][0] = i
    else : #col이 C, row가 distance
        block[distance][C] = i
# print('----------')
# print(block) : 맞게 들어있는 것으로 확인됨
#동근이의 위치, 거리
direct, distance = map(int, input().split()) #2,3
#동근이의 위치로 시작 좌표를 잡고, 순회해야함 #distance를 기반으로 row/col을 확인하고, direct로 idx확인
row, col = find_start(direct, distance) #시작 좌표를 찾고


result = min_block(row,col,block)
print(result)