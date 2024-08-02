import sys
#꽃가루 개수만큼 상하좌우의 풍선이 추가로 터진다 -> 다 터지는게 아니다...
sys.stdin = open('input9490.txt')

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    #최대값 출력
    arr = [list(map(int, input().split())) for _ in range(N)] #행의 개수만큼 input 받음
    data_row = [0, 1, 0, -1] #0, 2, 0, -2 #기존에 *2
    data_column = [1, 0, -1, 0] #2, 0, -2, 0

    total = 0
    for row in range(len(arr)):
        for col in range(len(arr[row])):

            s = 0
            for k in range(len(data_column)):
                for flower_index in range(arr[row][col]):
                    move_row = row + data_row[k] * flower_index
                    move_col = col + data_column[k] * flower_index

                    if 0<= move_row < N and 0 <= move_col < M:
                        s += arr[move_row][move_col]
                s += arr[row][col] # 나 자신의 값
            if s > total:
                total = s
    print(f'#{tc} {total}')