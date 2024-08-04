import sys

sys.stdin = open('input1954.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)] #네모난 크기의 배열 생성 -> 이제 값을 넣을 것
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]

    #이동하는 것이 있기 떄문에 이동전의 기준점 범위를 잡고 값을 더해줘야 함
    row, col, num, k = 0, 0, 1, 0 #0번쨰에는 값 1이들어가야함
    arr[row][col] = num
    num += 1
    #count가 N*N의 숫자를 넘기면 안됨
    while num <= N*N:
        move_row = row + data_row[k] #IndexError: list index out of range
        move_col = col + data_col[k]

        if 0<= move_row < N and 0<= move_col < N and arr[move_row][move_col] == 0:
            row, col = move_row, move_col
            arr[row][col] = num
            num += 1
        else :
            k = (k+1) % 4
    print(f'#{tc}')
    for a in arr:
        print(*a)