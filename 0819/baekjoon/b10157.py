import sys

sys.stdin = open('input10157.txt')
#테스트 케이스 개수
C, R = map(int, input().split())
K = int(input()) #찾는 좌석 번호
#일단 해당 내용을 기반으로 2차원 배열 초기화
seat = [[0]*C for _ in range(R)]
if K > C*R:
    print(0)
else :
    #방향전환 위치
    data_row = [-1, 0, 1, 0]
    data_col = [0, 1, 0, -1]

    row = R - 1
    direction = col = 0
    idx = 1
    while idx <= C * R :
        seat[row][col] = idx
        if idx == K:
            print(col+1, R - row)
            break

        move_row = row + data_row[direction]
        move_col = col + data_col[direction]
        if 0<=move_row<R and 0<=move_col<C and seat[move_row][move_col] == 0:
            row = move_row
            col = move_col
            idx += 1 #idx 순서 증가
        else :
            direction = (direction + 1) % 4
