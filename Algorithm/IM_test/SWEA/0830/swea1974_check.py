import sys

sys.stdin = open('input1974.txt')

#한줄씩 먼저 다 비교를 한다.
#한줄이 1~9의 합일 경우
#먼저 row 한줄 비교하기
def check_row(check_sum, sdocu, N):
    for row in range(N):
        total = 0
        for col in range(N):
            total += sdocu[row][col]
        if total != check_sum:
            return False
#            break #for 나가기
    return True #45가 아닌 값이 출력될 것

def check_col(check_sum, sdocu, N):
    for col in range(N):
        total = 0
        for row in range(N):
            total += sdocu[row][col]
        if total != check_sum:
            return False
    return True

def check_nine(check_sum, sdcou, N):
    #result = 0
    for j in range(0, N, 3): #total2를 확인안해도 될까?
        for i in range(0, N, 3):
            total = 0
            for row in range(0+j, 3+j):
                for col in range(0+i,3+i):
                    total += sdcou[row][col]
            if total != check_sum:
                return False
    return True


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = 9 #9*9스도쿠
    sdocu = [list(map(int, input().split())) for _ in range(N)] #9개씩 자른다.
    check_sum = sum([1, 2, 3, 4, 5, 6, 7, 8, 9])
    if check_row(check_sum,sdocu,N) and check_col(check_sum,sdocu,N) and check_nine(check_sum,sdocu,N):
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')
