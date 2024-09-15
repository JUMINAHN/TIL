import sys

def check_row_col(sdoku):
    #스도쿠를 탐색한다. -> 행먼저 -> 모두 탐색해야 함
    result = 1 #모든 행 열 에서 이상이 없어야 함
    for row in range(N):
        data = []
        for col in range(N):
            data.append(sdoku[row][col])
        if len(set(data)) != 9:
            result = 0 #a만약에 들어왔어 -> 그럼 그게 유지되는 것 -> 아닌게 하나 있다는 것
    return result #0인지 1인지 반환

def check_range(sdoku): #지금 5번 테케가 오류 -> 이 부분이 잘못된 것을 알 수 있음
    result3 = 1
    #파리퇴치처럼 3영역 구분 -> sdoku로 구분해야함
    for i in range(1, 4): #1, 2, 3
        for j in range(1, 4): #1, 2, 3
            data = []
            for row in range(3*(i-1), 3*i): #0, 3까지 -> 0, 1, 2
                for col in range(3*(j-1), j*3): #일단 오타 하나 확인 됨 -> #동일하게 진행 -> 0, 1, 2,
                    data.append(sdoku[row][col])
            if len(set(data)) != 9:
                result3 = 0
    return result3


sys.stdin = open('input1974.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1): #set으로 한꺼번에 묶을 수 있다.
    N = 9 # size 9*9짜리 스도쿠
    sdoku = [list(map(int, input().split())) for _ in range(N)] #스도쿠 내역 input받음
    result1 = check_row_col(sdoku) #행 탐색
    #열 -> 전치 행렬
    sdoku2 = list(map(list, zip(*sdoku)))
    result2 = check_row_col(sdoku2) #열 탐색
    result3 = check_range(sdoku)
    #파리퇴치처럼 3영역 구분 -> sdoku로 구분해야함

    if result1 == 0 or result2 == 0 or result3 == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')


