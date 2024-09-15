# 1. 델타 접근법 사용
# 2. sum에서 진행했던 것처럼 total에 최대값을 넣고, 출력되는 s값과 지속해서 비교하여 최대값 구하기
import sys

sys.stdin = open('input16268.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] #행의 개수 기준

    #각요소에 접근하기 전에 index 순회를 위한 data_row, column을 선언
    data_row = [0, 1, 0, -1]
    data_column = [1, 0, -1, 0]

    #index 순회를 통해 index 자체를 추출해야 함
    total = 0
    for row in range(len(arr)):
        for column in range(len(arr[row])):

            #index 모두를 순회할것
            s = 0
            for k in range(len(data_row)):
                move_row = row + data_row[k]
                move_column = column + data_column[k]

                #인덱스 범위를 벗어나는지 확인
                if 0<= move_row < N and 0<=move_column < M:
                    s += arr[move_row][move_column] #양 사방만 구하고 나를 구하지 않았음
            s += arr[row][column] #내 자신을 넣지 않았었음
            if total < s:
                total = s

    print(f'#{tc} {total}')