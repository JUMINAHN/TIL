#먼저 달팽이로 접근을 해보기로 했다. -> 11:50 ~ 12 : 24d // 12:58~
import sys
sys.stdin = open('input2564.txt')

def find_start(direct, distance):
    if direct == 1:  # 북, #row는 0, col의 위치가 distance(왼쪽으로 떨어진 위치
        block[0][distance - 1]  # idx를 기반으로 하기 위해서
        return 0, distance-1
    elif direct == 2:  # 남 #row는 R-1, col의 위치가 distance 상동
        block[R - 1][distance - 1]
        return R-1, distance-1
    elif direct == 3:  # 서쪽 #col의 위치가 0, row의 위치가 distance보다 1작음
        block[distance - 1][0]
        return distance-1, 0
    else:  # 상동이나 col의 위치가 R-1
        block[distance - 1][C - 1]
        return distance-1, C-1

def count_total(data_row, data_col):
    # 나의 시작점을 어떻게 잡을지는 direct와 distance 기준
    row, col = find_start(direct, distance)
    k = 0
    # 찾을 상점 번호 idx
    idx = 1
    move_count = 0
    while idx <= s_num:
        if block[row][col] == idx:  # 상점의 번호일 때
            idx += 1  # 다음 상점의 번호로 idx를 증가시켜주고
            break
        # 상점의 번호가 아니면 순회 시작을 위한 이동을 만들기
        move_row = row + data_row[k]
        move_col = row + data_col[k]
        if 0 <= move_row < R and 0 <= move_col < C:
            row = move_row
            col = move_col
            move_count += 1  # move를 이동할거에요
        else:
            k += 1
    return move_count

C, R = map(int, input().split()) #가로, 세로의 길이
block = [[0] * C for _ in range(C)] #block을 만든다.
s_num = int(input()) #상점의 개수 -> store_num
for i in range(1, s_num+1): #상점의 개수만큼도는데 원하는 idx가 들어가려면
    direct, distance = map(int, input().split()) #동서남북방향 / 거리
    if direct == 1: #북, #row는 0, col의 위치가 distance(왼쪽으로 떨어진 위치
        block[0][distance-1] = i #idx를 기반으로 하기 위해서
    elif direct == 2: #남 #row는 R-1, col의 위치가 distance 상동
        block[R-1][distance-1] = i
    elif direct == 3: #서쪽 #col의 위치가 0, row의 위치가 distance보다 1작음
        block[distance-1][0] = i
    else : #상동이나 col의 위치가 R-1
        block[distance-1][C-1] = i
#print(block)

direct, distance = map(int, input().split()) #동근이(경비원)의 위치 row,col로 나누어 접근하기

#오른쪽으로 가는게 우선인 경우
data_row1 = [0, -1, 0, 1]
data_col1 = [1, 0, -1, 0]
#total을 반환
right_first = count_total(data_row1, data_col1)

#왼쪽으로 가는게 우선인 경우,
data_row2 = [0, 1, 0, -1]
data_col2 = [-1, 0, 1, 0]
left_first = count_total(data_row2, data_col2)

if right_first < left_first:
    print(right_first)
else :
    print(left_first)

