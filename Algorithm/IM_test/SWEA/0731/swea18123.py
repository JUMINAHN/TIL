import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    data_r = [0, 1, 0, -1]
    data_c = [1, 0, -1, 0]

    total = 0 #총합을 구하기 위해선 모든 값을 다 순회해야 총합을 구해지니까 -> 이곳에 선언 --> "모두 조사"
    for row in range(len(arr)):
        for column in range(len(arr[row])):

            s = 0 #이건 맞다고 생각해 -> 상하좌우의 값을 더하기 위해서
            for k in range(len(data_r)):
                move_row = row + data_r[k]
                move_column = column + data_c[k] #오타 주의

                if 0<=move_row<N and 0<=move_column<N:
                    s += abs(arr[move_row][move_column] - arr[row][column])
            total += s
    print(f'#{tc} {total}')