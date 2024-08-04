import sys

sys.stdin = open('input1954.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #N*N사이즈

    arr = [[1]*N for _ in range(N)] #배열이 만들어져있다 --> 이곳에 값을 채워 넣자
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]

    num=1
    for row in range(N):
        if num == (N * N):
            break
        for col in range(N):
            for k in range(len(data_row)):
                move_row = row + data_row[k]
                move_col = col + data_col[k]
                if 0<=move_row<N and 0<=move_col<N and arr[move_row][move_col] == 1:
                    num += 1
                    arr[move_row][move_col] = num
                    break
                else:
                    continue
    print(f'#{tc}')
    for a in arr:
        print("".join(map(str, a)))