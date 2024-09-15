
C, R = map(int, input().split())
K = int(input())
seat = [[0]*C for _ in range(R)]

data_row = [-1,0,1,0]
data_col = [0,1,0,-1]

if K > C*R:
    print(0)
else :
    row = R-1 #밑에서 부터 접근하기 떄문에 -> row값이 고정되어있어서
    col = 0

    direction = 0
    idx = 1
    #숫자가 42를 넘으면 안돼

    while idx <= C * R:
        seat[row][col] = idx
        if idx == K:
            print(col+1, R-row)
            break
        move_row = row + data_row[direction]
        move_col = col + data_col[direction]
        if 0<=move_row<R and  0<=move_col<C and seat[move_row][move_col] == 0:
            row = move_row
            col = move_col
            idx += 1 #이동하니까 값이 증가됨
        else : #방향 변경
            direction = (direction+1) % 4
    #print(seat)
