#import sys
#sys.stdin = open('input10157.txt')

C, R = map(int, input().split()) #x,y좌표
K = int(input()) #찾는 친구
seat = [[0]*C for _ in range(R)]
#print(seat) #거기에 맞는 친구들을 대입해준다.
#달팽이로 돌아보자
data_row = [-1, 0, 1, 0]
data_col = [0, 1, 0, -1]
if K > C*R: #초기 설정
    print(0)
else :
    idx = 1
    start_row = R-1
    start_col = 0
    k = 0
    while idx <= R*C:
        seat[start_row][start_col] = idx
        if idx == K:
            print(start_col + 1, R - start_row)
            break
        move_row = start_row + data_row[k] #오탈자 잘보기
        move_col = start_col + data_col[k]

        if 0 <= move_row < R and 0 <= move_col < C and seat[move_row][move_col] == 0:
            idx += 1
            start_row = move_row
            start_col = move_col
        else :
            k = (k+1) % 4

    if idx > R*C:
        print(0)
