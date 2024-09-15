import sys

sys.stdin = open('input12712.txt')

def sqaure(N, M, pari):
    #정방향 data_row, col 구분
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]
    #일단 정방형 + 노즐 기반으로 가장 큰 값 구하기
    total_max = 0
    #모든 노즐은 일단 탐색
    for row in range(N):
        for col in range(N):
            four_sum = 0
            for k in range(len(data_row)):
                for i in range(1, M):
                    move_row = row + data_row[k] * i #1번만큼 분사
                    move_col = col + data_col[k] * i
                    if 0 <= move_row < N and 0 <= move_col < N:
                        four_sum += pari[move_row][move_col] #네개가 더해짐
            four_sum += pari[row][col] #가운데에 있는 파리 더해짐
            if total_max < four_sum:
                total_max = four_sum #가장 큰 값 전달하기
    return total_max

def cross1(N,M,pari): #하나로 봤으면 되었는데,, 실수를 했다
    data_row = [1, 1, -1, -1]
    data_col = [1, -1, -1, 1]
    #일단 대각선 왼 -> 오 노즐 기반으로 가장 큰 값 구하기
    total_max = 0
    #모든 노즐은 일단 탐색
    for row in range(N):
        for col in range(N):
            two_sum = 0
            for k in range(len(data_row)):
                for i in range(1, M):
                    move_row = row + data_row[k] * i #1번만큼 분사
                    move_col = col + data_col[k] * i
                    if 0 <= move_row < N and 0 <= move_col < N:
                        two_sum += pari[move_row][move_col] #네개가 더해짐
            two_sum += pari[row][col] #가운데에 있는 파리 더해짐
            if total_max < two_sum:
                total_max = two_sum #가장 큰 값 전달하기
    return total_max

# def cross2(N,M,pari):
#     data_row = [1, -1]
#     data_col = [-1, 1]
#     #일단 대각선 왼 -> 오 노즐 기반으로 가장 큰 값 구하기
#     total_max = 0
#     #모든 노즐은 일단 탐색
#     for row in range(N):
#         for col in range(N):
#             two_sum = 0
#             for k in range(len(data_row)):
#                 for i in range(1, M):
#                     move_row = row + data_row[k] * i #1번만큼 분사
#                     move_col = col + data_col[k] * i
#                     if 0 <= move_row < N and 0 <= move_col < N:
#                         two_sum += pari[move_row][move_col] #네개가 더해짐
#             if total_max < two_sum:
#                 total_max = two_sum #가장 큰 값 전달하기
#     return total_max

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split()) #배열의 크기, 파리 공간
    pari = [list(map(int, input().split())) for _ in range(N)] #파리 개체 다 input
    one_result = sqaure(N,M, pari) #십자가 모양 결과물
    two_result1 = cross1(N,M,pari)
    # two_result2 = cross2(N,M,pari)
    cross_result = two_result1

    if one_result > cross_result :
        print(f'#{tc} {one_result}')
    else :
        print(f'#{tc} {cross_result}')
    #print(one_result)