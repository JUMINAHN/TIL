import sys

sys.stdin = open('input1209.txt')
#테스트 케이스 개수
#정방형을 모두 더했을떄
def rowcol(arr, N):
    max = 0
    for row in range(N):
        col_max = 0
        row_max = 0
        for col in range(N):
            col_max += arr[row][col]
            row_max += arr[col][row]

        if max < col_max:
            max = col_max
        if max < row_max:
            max = row_max
    return max

#일단 정방형 cross부터
def cross(arr, N):
    sum1 = 0
    sum2 = 0
    for i in range(N):
        sum1 += arr[i][i]
        sum2 += arr[i][N-1-i]
    if sum1 > sum2:
        return sum1
    else:
        return sum2

T = 10
for tc in range(1, T+1):
    #100 * 100의 2차원 배열이 주어질 때, 각행의 합/열/대각선 중 최대값을 구하는 프로그램 작성
    test_case = int(input())
    N = 100 #배열의 크기가 100*100으로 고정되어있기 떄문에
    arr = [list(map(int, input().split())) for _ in range(N)] #0부터 99까지 생성되는 것이기 떄문에 N = 100이 맞을텐데..?
    #row, col의 최대값을 구한다
    rowcol_max = rowcol(arr, N)
    cross_max = cross(arr, N)
    if rowcol_max > cross_max:
        print(f'#{test_case} {rowcol_max}')
    else :
        print(f'#{test_case} {cross_max}')