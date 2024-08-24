import sys

sys.stdin = open('input1216.txt')
#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    N = 100
    test_case = int(input())
    arr = [list(input()) for _ in range(N)]

    max_length = 0
    #행 기준
    for row in range(N): #0부터 99까지 돌릴 것
        num = 0
        for i in range(num, N):
            row_check = []
            for col in range(num, i): #0부터 i까지 --> 2부터 2까지일수도 있고, 이 부분이 잘못된듯
                row_check.append(arr[row][col])
            reverse_row = row_check[::-1]
            if row_check == reverse_row:
                if max_length < len(row_check):
                    max_length = len(row_check)
        num += 1 #num을 증가시킨다.

    #열 기준
    for col in range(N):
        num = 0
        for i in range(num, N):
            col_check = []
            for row in range(i): #0부터 i까지
                col_check.append(arr[row][col])
            reverse_row = col_check[::-1]
            if col_check == reverse_row:
                if max_length < len(col_check):
                    max_length = len(col_check)
        num += 1

    print(f'#{test_case} {max_length}')