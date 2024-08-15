# import sys
#
# sys.stdin = open('input1.txt')
#테스트 케이스 개수
T = int(input()) #3번
for tc in range(1, T+1):
    #1. 미생물 먹이
    #2. 델타
    #3. 마이너스값이 나올경우 그 중에 가장 큰 값 (마이너스 중에서 가장 작은 값)

    N = int(input())
    #미생물이 들어있는 칸을 생성
    arr = [list(map(int, input().split())) for _ in range(N)]

    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]

    #음수일떄도 가능성이 있으니 max_num을 맨처음에 합산된 값을 기준으로 넣어주자
    max_num = 0
    for row in range(N):
        for col in range(N):
            detal_sum = 0
            for k in range(len(data_row)):
                move_row = row + data_row[k]
                move_col = col + data_col[k]

                if 0<=move_row<N and 0<=move_col<N:
                    detal_sum += arr[move_row][move_col]
            detal_sum += arr[row][col] #나의 값

            if row == 0 and col == 0: #초기값을 세팅하겠다. -> 세팅해줌으로써 문제 해결결
               max_num = detal_sum
            if max_num < detal_sum:
                max_num = detal_sum
    print(f'#{tc} {max_num}')