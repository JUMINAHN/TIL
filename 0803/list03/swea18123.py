#row, colum 똑같은 배열
import sys

sys.stdin = open('input18123.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)] #2차원 배열 만들어짐
    #우측 기준
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]

    total = 0
    for row in range(N):
        for col in range(N): #deltal네요..
            #이동할겁니다
            s = 0 #하나의 사분면 탐색 -> 절대값들이 더해져요
            for k in range(len(data_row)):
                move_row = row + data_row[k]
                move_col = col + data_col[k]

                if 0 <= move_col < N and 0 <= move_row < N: #오른쪽부터 --> 이동하는 idx 색칠됨
                    #그런데 이문제는 나와 새로운 값 비교
                    s += abs(arr[move_row][move_col] - arr[row][col])
            total += s
            
    print(f'#{tc} {total}')