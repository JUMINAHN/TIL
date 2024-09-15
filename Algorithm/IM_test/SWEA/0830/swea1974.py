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
            return total
#            break #for 나가기
    return check_sum #45가 아닌 값이 출력될 것

def check_col(check_sum, sdocu, N):
    for col in range(N):
        total = 0
        for row in range(N):
            total += sdocu[row][col]
        if total != check_sum:
            return total
    return check_sum

def check_nine(check_sum, sdcou, N):
    result = 0
    for i in range(0, N, 3):
        total = 0
        for row in range(0, 3):
            for col in range(0,3):
                total += sdcou[row][col]
        if total != check_sum:
            result = total
            break
        else :
            result = total

    result1 = 0
    for i in range(0, N, 3):
        total = 0
        for row in range(0, 3):
            for col in range(3,6):
                total += sdcou[row][col]
        if total != check_sum:
            break
        else :
            result1 = total

    result2 = 0
    for i in range(0, N, 3):
        total = 0
        for row in range(0, 3):
            for col in range(6,9):
                total += sdcou[row][col]
        if total != check_sum:
            break
        else :
            result2 = total

    if result != check_sum or result1 != check_sum or result2 != check_sum:
        return 0
    else :
        return check_sum

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = 9 #9*9스도쿠
    sdocu = [list(map(int, input().split())) for _ in range(N)] #9개씩 자른다.
    check_sum = sum([1, 2, 3, 4, 5, 6, 7, 8, 9])
    #print(check_nine(check_sum, sdocu,N))
    #print(check_row(check_sum, sdocu, N))
    #print(check_col(check_sum, sdocu, N))
# #checkrow, checkcol,checknine 그리고 나머지 중 45가 아닌게 한개라도 있으면 0을 반환하는 것으로
    if check_row(check_sum,sdocu,N) != check_sum or check_col(check_sum,sdocu,N) != check_sum or check_nine(check_sum,sdocu,N) != check_sum :
        print(f'#{tc} 0')
    else :
        print(f'#{tc} 1')
