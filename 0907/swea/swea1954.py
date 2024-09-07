import sys

sys.stdin = open('input1954.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    #달팽이 그자체

    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]
    row = col = direct = 0
    idx = 1 #1부터 시작
    while idx <= N*N:
        arr[row][col] = idx
        if idx == N*N: #그냥 값만 채우고 break해야 밑에 조건을 실행하지 않기 떄문에, 범위 초과 유발 가능성
            break
        move_row = row + data_row[direct]
        move_col = col + data_col[direct]
        if 0<=move_row<N and 0<=move_col<N and arr[move_row][move_col] == 0:
            row = move_row
            col = move_col
            idx += 1
        else : #방향 전환
            direct = (direct + 1) % 4
    print(f'#{tc}')
    for a in arr:
        print(*a)