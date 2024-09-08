#import sys
#sys.stdin = open('input1018.txt')

def find_color(data, chess_WB):
    total = 0 #셀거에요
    for row in range(eight):
        for col in range(eight):
            if data[row][col] != chess_WB[row][col]:
                total += 1
    return total #다른 것들을 셀거에요

#체스판
#M * N크기의 보드
#어떤 정사각형은 검정색, 나머지는 흰색
# M*N의 크기중 일부를 추출해서 -> 8*8크기의 체스판을 만드려고 한다.
# 체스판은 검정색과 흰색이 번갈아서 칠해져있어야 한다. -> 검정/흰색 다른색으로
    #즉 맨왼쪽위칸이 흰색이거나 거멍색인 경우
    #모든 보드가 체스판처럼 칠해져있다는 보장이 없어서 지민이는 8*8의 크기로 잘라내고 정사각형을 다시칠해야겠다고 마음을 먹었따.
    #최소개수
eight = 8
N, M = map(int, input().split())
square = [list(input()) for _ in range(N)] #여기서 8씩 추출해야 함
#특정 체스판 -> 흰색이 먼저인것을 먼저 작성하고, 그 기준을 바탕으로 검정색이 먼저인것도 만들어보자 일단 흰색
chess_W = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
         ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
         ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
#print(square)
chess_B = chess_W[::-1]
#print(chess_B)


#일단 파리퇴치처럼 점검할 범위 -> 왜냐하면 보드판이 더 작을 수 있기 떄문에
min_num = eight * eight
for i in range(0, N - eight + 1):
    for j in range(0, M - eight + 1):
        #여기서는 원하는 영역만큼 돌아간다.
        #따라서 특정 체스판과 이 input값이 같은지확인하고, 아니라면 아닌 것에 대해서 count를 해주는 것
        count_w = 0
        find_data = [] #여기서 얻은 find_data와 white / black의 최소차이를 비교하는 것
        for row in range(i, i+eight):
            data = []
            for col in range(j, j+eight):
                data.append(square[row][col])
            find_data.append(data)
        white = find_color(find_data, chess_W)
        black = find_color(find_data, chess_B)
        diff = min(white, black)
        if min_num > diff:
            min_num = diff

print(min_num)


#범위가 같을때만 해당 됨,
# for row in range(i, i + eight):
#     for col in range(j, j + eight):
#         if square[row][col] != chess_W[row][col]:
#             count_w += 1  # 같지 않은 것들 count해주기
# # black먼저
# count_b = 0
# for row in range(i, i + eight):
#     for col in range(j, j + eight):
#         if square[row][col] != chess_B[row][col]:
#             count_b += 1  # 같지 않은 것들 count해주기