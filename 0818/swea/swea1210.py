import sys

sys.stdin = open('input1210.txt')

def find_start(ladder, S):
    for row in range(S):
        for col in range(S):
            if ladder[row][col] == 2:
                return row,col

#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    test_case = int(input())
    S = 100
    ladder = [list(map(int, input().split())) for _ in range(S)]
    #출발 좌표를 찾고 그 위치를 기반으로 사다리타기를 시작한다.
    #밑에서 위로 가는 방향이며, 우선순위는 좌 or 우, 후순위가 위이다.
    #방향전환은 총 3개만 진행하면 된다.

    #방향전환
    data_row = [0, 0, -1]
    data_col = [1, -1, 0]


    #먼저 2가 있는 출발 좌표를 알아봐야 함
    #row,col 확인 (뒤에서 부터 접근)
    row, col = find_start(ladder, S)

    while row != -1 : #row가 0일때까지
        ladder[row][col] = 0 #왔던길을 다시 돌아오지 않게 하기 위해서
        if row == 0:
            break

        for direction in range(len(data_row)):
            move_row = row + data_row[direction]
            move_col = col + data_col[direction]
            if 0 <= move_row < S and 0 <= move_col < S and ladder[move_row][move_col] != 0:
                row = move_row #아니면 이동한다.
                col = move_col
    print(f'#{test_case} {col}')