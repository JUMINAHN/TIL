import sys

sys.stdin = open('input10760.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    #맨오른쪽부터 -> 회전할 위치
    data_row = [0,1,1,1,0,-1,-1,-1]
    data_col = [1,1,0,-1,-1,-1,0,1]
    space = [list(map(int, input().split())) for _ in range(N)]


    total_count = 0
    for row in range(N):
        for col in range(M):
            stand = space[row][col]

            check_point = 0
            for k in range(len(data_row)):
                move_row = row + data_row[k]
                move_col = col + data_col[k]
                if 0<=move_row<N and 0<=move_col<M and space[move_row][move_col] < stand:
                    check_point += 1 #찾으면 checkpoint 증가
            if check_point >= 4: #4방향이상이면 됨
                total_count += 1
    print(f'#{tc} {total_count}')