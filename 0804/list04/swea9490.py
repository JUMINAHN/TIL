import sys

sys.stdin = open('input9490.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N줄에 걸쳐 M개씩 들어있는 꽃가루 개수 -> 한개의 최대 풍선 꽃가루의 합
    arr = [list(map(int, input().split())) for _ in range(N)] #행의 개수

    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]

    total = 0
    for row in range(N):
        for col in range(M):
            attack = arr[row][col] #현재 꽃가루 개수 --> 추가로 터질 꽃가루 개수
            s = 0

            for a in range(1, attack+1):
                for k in range(len(data_row)):
                    move_row = row + data_row[k] * a
                    move_col = col + data_col[k] * a

                    if 0 <= move_row < N and 0 <= move_col < M:
                        s += arr[move_row][move_col]
            #나 자신의 값
            s += arr[row][col]

            if total < s:
                total = s
    print(f'#{tc} {total}')
