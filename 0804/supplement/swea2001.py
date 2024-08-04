import sys

sys.stdin = open('input2001.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for row in range(N-M+1): #범위설정
        for col in range(N-M+1):
            s = 0
            for sub_row in range(row, row+M): #범위설정
                for sub_col in range(col, col+M):
                   s += arr[sub_row][sub_col]
            if total < s :
                total = s
    print(f'#{tc} {total}')