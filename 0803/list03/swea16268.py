import sys

sys.stdin = open('input16268.txt')

#delta
# 내값까지 더해줘야 함
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #row, col
    arr = [list(map(int, input().split())) for _ in range(N)]
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]

    total_max = 0
    for row in range(N):
        for col in range(M):
            s = 0
            for k in range(len(data_row)):
                move_row = row + data_row[k]
                move_col = col + data_col[k]

                if 0<= move_row < N and 0 <= move_col < M:
                    s += arr[move_row][move_col]
            s += arr[row][col]

            if total_max < s:
                total_max = s
    print(f'#{tc} {total_max}')
