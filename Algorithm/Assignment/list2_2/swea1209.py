#행 / 열 / 대각선
import sys

sys.stdin = open('input1209.txt')
def max_row_col(arr):
    #모든 행을 더하는 함수 -> 열도 동일함
    max_row = max_col = 0
    for row in range(N):
        r = c = 0
        for column in range(N):
            r += arr[row][column]
            c += arr[column][row] #개수가 똑같으면 위치만 바꾸면 된다. -> 정사각형의 장점
        if r > max_row : #지금 행의 누적 값이 더 크다면
            max_row = r
        if c > max_col : #지금 열의 누적 값이 더 작다면
            max_col = c
    #결과론적으로 max와 col중에 더 큰 것 반환`
    if max_row > max_col : #max_row 반환
        return max_row
    else :
        return max_col

#cross -> 대각선 기준 더 큰 대각선 추출
def max_cross(arr):
    max_cross1 = max_cross2 = 0
    for row in range(N):
        max_cross1 += arr[row][row] #대각선 자체
        max_cross2 += arr[row][N-1-row] #반대 대각선 자체
    if max_cross1 > max_cross2 :
        return max_cross1
    else :
        return max_cross2

T = 10
for tc in range(1, T+1):
    num = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)] #2차원 리스트 만들기
    row_col = max_row_col(arr) #행열 중에 더 큰 것
    max_cro = max_cross(arr)
    if max_cro > row_col:
        print(f'#{tc} {max_cro}')
    else :
        print(f'#{tc} {row_col}')

