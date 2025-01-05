import sys

sys.stdin = open('input1954.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    print(f'#{tc}')

    row = col = direct = 0
    #방향 전환
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]

    idx = 1
    while idx <= N*N : #9넘어가면 종료
        arr[row][col] = idx
        if idx == N*N:
            break
        move_row = row + data_row[direct]
        move_col = col + data_col[direct]
        if 0<=move_row<N and 0<=move_col<N and arr[move_row][move_col] == 0:
            #가능하게
            row = move_row
            col = move_col
            idx += 1 #idx도 증가
        else : #그게 아니면
            direct = (direct + 1 ) % 4
    for a in arr:
        print(" ".join(map(str, a)))
    #칸 별 이름 채우기