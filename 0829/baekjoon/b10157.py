import sys

sys.stdin = open('input10157.txt')
#테스트 케이스 개수
T = int(input()) #testcase
for tc in range(1, T+1):
    C, R = map(int, input().split())
    find = int(input())
    seat = [[0]*C for _ in range(R)]
    #print(seat)
    #seat를 만들고, 그 안에 값을 채워넣는다.
    if find > C*R:
        print(0)
    else:
        #이동 방향
        data_row = [-1, 0, 1, 0]
        data_col = [0, 1, 0, -1]
        #초기값 세팅
        row = R-1
        col = direct = 0
        idx = 1 #1부터 시작
        #idx가 증가하지 않는다..
        while idx <= C*R: #C*R을 넘으면 종료
            seat[row][col] = idx  # idx를 넣는다.
            if idx == find:
                break

            move_row = row + data_row[direct]
            move_col = col + data_col[direct]
            if 0 <= move_row < R and 0 <= move_col < C and seat[move_row][move_col] == 0: #0일때만 접근 가능
                row = move_row
                col = move_col #바꿔준다.
                idx += 1
            #아니라면 방향 전환
            else :
                direct = (direct + 1) % 4
        #현재의 row, col 출력 근데 1부터시작하니까 다 +1, C, R로
        print(R-row, col+1) #역순이기 떄문에
        #print(seat)