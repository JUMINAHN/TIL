import sys

sys.stdin = open('input2001.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    parichae_row = [i for i in range(M)] #0, 1
    parichae_column = [i for i in range(M)] #0,1

    total = 0
    for row in range(N):
        for column in range(len(arr[row])):

            s = 0
            for k in range(len(parichae_row)):
                move_row = row + parichae_row[k]
                for ok in range(len(parichae_column)):
                    move_column = column + parichae_column[ok] #column의 값이 바뀌니까
                    if 0 <= move_row < N and 0 <= move_column < N:
                        s += arr[move_row][move_column]

            if total < s :
                total = s
    print(f'#{tc} {total}')
