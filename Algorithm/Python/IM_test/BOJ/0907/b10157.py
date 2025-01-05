#import sys
#전형적인 달팽이 문제
#sys.stdin = open('input10157.txt')
# #테스트 케이스 개수
# T = int(input())
# for tc in range(1, T+1):
C, R = map(int, input().split())
K = int(input()) #찾는 숫자
seat = [[0]*C for _ in range(R)]

#달팽이 시작
if C*R < K:
    print(0)
else :
    data_row = [-1, 0, 1, 0]
    data_col = [0, 1, 0, -1]
    row = R - 1
    col = direct = 0
    idx = 1

    while idx <= C*R:
        seat[row][col] = idx
        #print(seat)
        if idx == K or idx >= C*R: #찾았다 나가자 -> 마지막 값이 동일할 경우 -> 범위 제대로
            break
        move_row = row + data_row[direct]
        move_col = col + data_col[direct]
        if 0<=move_row<R and 0<=move_col<C and seat[move_row][move_col] == 0: #오타!! 자신에게 확신을 가지길..
            row = move_row
            col = move_col
            idx += 1
        else :
            direct = (direct + 1) % 4
    print(col+1, R-row)
#30이 6,5가 되어야 함