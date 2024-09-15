import sys

sys.stdin = open('input1209.txt')
# Testcase 수
# Testcase 만큼 반복
def check_row(N, arr):
    max_sum = 0
    for row in range(N):
        col_sum = 0
        for col in range(N):
            col_sum += arr[row][col]
        if max_sum < col_sum:
            max_sum = col_sum
    return max_sum

def check_col(N, arr):
    max_sum = 0
    for col in range(N):
        row_sum = 0
        for row in range(N):
            row_sum += arr[row][col]
        if max_sum < row_sum:
            max_sum = row_sum
    return max_sum

#왼-> 오 대각선
def cross1(N,arr):
    total_sum = 0
    for i in range(N):
        total_sum += arr[i][i]
    return total_sum

#오 -> 왼 대각선
def cross2(N,arr):
    total_sum = 0
    for i in range(N):
        total_sum += arr[i][N-1-i]
    return total_sum

T = 10
for tc in range(1, T+1):
    SIZE = 100
    #동일한 최대값이 있을 경우 하나만 출력한다.
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(SIZE)]
    #최대값 출력
    result = max(cross1(SIZE, arr), cross2(SIZE, arr), check_row(SIZE, arr), check_col(SIZE, arr))
    print(f'#{test_case} {result}')


    #모든 행 탐색
    #모든 열 탐색
    #cross 1 탐색
    #cross 2 탐색
