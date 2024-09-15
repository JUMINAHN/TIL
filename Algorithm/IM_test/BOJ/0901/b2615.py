#9시1분인데도 해결못함
#4시 40분부터 ~ 5시 36분까지 일단 1차
# import sys
# sys.stdin = open('input2615.txt')
#3,4
def check_color(N, arr, color):
    data_row = [[0, 1], [1, 0], [1, 1], [1, -1]]  # 가로, 세로, 대각선(우하향), 대각선(좌하향)
    data_col = [[1, 0], [0, 1], [1, 1], [-1, 1]]

    for row in range(N):
        for col in range(N):
            if arr[row][col] == color:
                for d in range(len(data_row)):
                    check_count = 1
                    for i in range(1, 5):
                        move_row = row + data_row[d][0] * i
                        move_col = col + data_col[d][0] * i
                        if 0 <= move_row < N and 0 <= move_col < N and arr[move_row][move_col] == color:
                            check_count += 1
                        else:
                            break

                    if check_count == 5:
                        # 6목 체크
                        prev_row = row - data_row[d][0]
                        prev_col = col - data_col[d][0]
                        next_row = row + data_row[d][0] * 5
                        next_col = col + data_col[d][0] * 5

                        if (prev_row < 0 or prev_row >= N or prev_col < 0 or prev_col >= N or arr[prev_row][
                            prev_col] != color) and \
                                (next_row < 0 or next_row >= N or next_col < 0 or next_col >= N or arr[next_row][
                                    next_col] != color):
                            return row, col, color
    return 0, 0, 0


N = 19
B = 1
W = 2
K = 5
 #값도 잘 올라갔고 아까 잘 담겼는데 왜 여기에 다르게 들어왔지?
arr = [list(map(int, input().split())) for _ in range(N)]
row2, col2, color2 = check_color(N,arr,B) #지금 맞게 담겼어 4,3,1이
#자체 debugging을 했들때 4, 3,1 담겨있었는데 지금 확인하니까 4, 1, 0이 담기는지?
row1, col1, color1 = check_color(N,arr,W) #값이 다 잘 담겼어

# if (color1 == 0 and color2 == 0) or (color1 != 0 and color2 != 0):
#     print(0)
# elif color1 != 0:
#     print(color1)
#     print(row1 + 1, col1 + 1)
# elif color2 != 0:
#     print(color2)
#     print(row2 + 1, col2 + 1)

result_color = result_col = result_row = 0
#만약 color가 둘다 0이거나 color1과 color2가 값이 있는 경우
if (color1 == 0 and color2 == 0) or (color1 != 0 and color2 != 0):
    result_color = 0
elif color1 != 0:
    result_color = color1
    result_row = row1
    result_col = col1
elif color2 != 0:
    result_color = color2
    result_row = row2
    result_col = col2
#
# #이 전에 color가 담기는지 보기
# #그리고
if result_color == 0: #result_color에 담기는게 없을 때 == 0 그리고, white랑 black랑 동일할 때
    print(0)
else : #해당 되는 color가 없다면
    final_row = N #가장 큰 값으로 설정해놓고
    final_col = N
    for row in range(N):
        for col in range(N):
            if arr[row][col] == result_color:
                if col < final_col or (col == final_col and row < final_row):
                    final_row = row
                    final_col = col
    print(result_color)
    print(final_row + 1, final_col + 1)
#     found = False
    #원래 코드: row만 범위를 설정하고 col은 항상 0
    # row와 col이 바둑판 범위 내에 있는지 직접 확인
    #max(0, result_row - 2): result_row - 2가 음수가 되면 0으로 설정
    # min(N, result_row + 3): result_row + 3이 N을 넘어가면 N으로 제한
#     for row in range(max(0, result_row - 2), min(N, result_row + 3)): #조건문을 없애버리는 것
#         for col in range(max(0, result_col - 2), min(N, result_col + 3)):
#             if arr[row][col] == result_color: #row가 0이면 첫번쨰로 발견한 돌 -> final row가 0이면 아직 발견하지 않았따는 것이니까
#                 #현재 돌의 열(col)이 이전에 저장한 돌의 열(final_col)보다 작은지 확인
#                 #if final_row == 0 or col < final_col or (col == final_col and row < final_row): #현재 돌의 열(col)이 이전에 저장한 돌의 열(final_col)보다 작은지 확인
#                 if col < final_col or (col == final_col and row < final_row): #이거 도대체먼데
#                      final_row = row #더 작은 것
#                      final_col = col
#     print(result_color)
#     print(final_row+1, final_col+1) #idx자체가 틀렸음
# #         if found : #이거 꿀팁!!!
# #             break
#         for col in range(1):#col은 0이어야 함 -> 맨왼쪽꺼 먼저
#             #이것도 범윌 벗어날 위험이 있기 떄문에 추가로
#             if 0<= row < N and 0 <= col < N and arr[row][col] == result_color:
#                 final_row = row #맨 첫번쨰로 들어가는 것
#                 final_col = col
#                 found = True #이렇게 조건을 쉽게 설정하면 됨!!! 이건 꿀팁 이상한 조건으로 값을 빠져나갈 일이 없음
#                 break #co
#

