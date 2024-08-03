# 정방향
import sys

sys.stdin = open('input2001.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N은 나의 전체크기고, M은 찾고자하는 크기
    arr = [list(map(int, input().split())) for _ in range(N)] #5*5 -> 정방향
    data_row = [0, 1, 1]
    data_col = [1, 1, 0] #*M?

    total = 0
    for row in range(N):
        for col in range(N):
            s = 0
            for sub in range(1, M+1):
                for k in range(len(data_row)): #이렇게 하면 범위 한쪽만 됨
                    move_row = row + data_row[k] * sub
                    move_col = col + data_col[k] * sub

                    if 0 <= move_row < N and 0 <= move_col < N: #여기에 들어가지 않음
                        s += arr[move_row][move_col]
                s += arr[row][col] #내 값도 넣어줘야 함
            if total < s:
                total = s
    print(f'#{tc} {total}')

