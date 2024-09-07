import sys
#10시 30분 ~ 11시 7분
sys.stdin = open('input1.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    r1,c1,r2,c2 = map(int, input().split()) #1,1,3,4 색칠한 영역만 확인하기
    arr = [list(map(int, input().split())) for _ in range(N)] #잔디에 값을 넣기

    #평탄화 높이의 합
    height_sum =0
    for row in range(r1, r2+1):
        for col in range(c1, c2+1):
            height_sum += arr[row][col]
    area_num = (r2-r1+1)*(c2-c1+1)
    aver = height_sum // area_num

    for row in range(r1, r2+1):
        for col in range(c1, c2+1):
            num = arr[row][col]
            if num == aver:
                continue
            else :



    # count = 0
    #
    # check_point = [0] * 11
    # while check_point[aver] != area_num:
    #     check_point = [0] * 11
    #     max_num = 0
    #     max_row = 0
    #     max_col = 0
    #
    #     min_num = float('inf')
    #     min_row = float('inf')
    #     min_col = float('inf')
    #     #색종이 만큼 돌기
    #     #가장 작은 값들 담아서
    #     for row in range(r1, r2+1):
    #         for col in range(c1, c2+1):
    #             num = arr[row][col]
    #             if max_num < num:
    #                 max_num = num
    #                 max_row = row
    #                 max_col = col
    #             if min_num > num:
    #                 min_num = num
    #                 min_row = row
    #                 min_col = col
    #     #가장 큰것 -1
    #     arr[max_row][max_col] -= 1
    #     #가장 작은 것 -1
    #     arr[min_row][min_col] += 1
    #     count += 1

