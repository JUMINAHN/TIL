import sys

sys.stdin = open('input1210.txt')

def find_start(S, ladder):
    for row in range(99, 98, -1):
        for col in range(S):
            if ladder[row][col] == 2:
                return col

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    test_case = int(input())
    S = 100 #size 100
    ladder = [list(map(int, input().split())) for _ in range(S)] #ladder의 크기만큼

    # ladder 순회
    # 순회전 start 위치 확인 필요
    #좌표값의 위치 확인을 위해
    start_col = find_start(S, ladder)
    start_row = S-1

    #이동하기 위한 좌표, 이동방향 설정
    data_row = [0, 0, -1] #왼쪽부터 시작
    data_col = [-1, 1, 0]
    while start_row != 0 : #0에 도착할때까지
        ladder[start_row][start_col] = 0 #되돌아가지 않기 위해 초기화
        for k in range(len(data_row)):
            move_row = start_row + data_row[k]
            move_col = start_col + data_col[k]
            if 0<= move_row < S and 0<=move_col < S and ladder[move_row][move_col] == 1: #1인 위치에만 가능하다.
                start_row = move_row
                start_col = move_col
    print(f'#{test_case} {start_col}')