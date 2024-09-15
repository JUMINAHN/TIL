import sys

#델타.. 근데 나는 델타는 생각이 안남
#오목 행->열-> 대각선
sys.stdin = open('input11315.txt')

#뭔가 else에서 초기화시켜서 그런듯
def rowcol(N, arr):
    # 행 / 열 비교
    for row in range(N):
        col_total = 0
        row_total = 0
        for col in range(N):
            if arr[row][col] == 'o':
                col_total += 1
            else:
                if col_total >= 5 :
                    return True  # YES -> True 반환
                    break
                col_total = 0

            if arr[col][row] == 'o':
                row_total += 1
            else:
                if row_total >= 5:
                    return True  # YES -> True 반환
                    break
                row_total = 0
        if col_total >= 5 or row_total >= 5:
            return True #YES -> True 반환
            break
    return False

def cross(N, arr):
    #대각선 비교
    count1 = 0 #조건이 초기화되고 있는 문제를 확인해서 밖으로 뺏다.
    count2 = 0
    for i in range(N):
        if arr[i][i] == 'o':
            count1 += 1
        else :
            if count1 >= 5:
                return True
                break
            count1 = 0

        if arr[i][N-1-i] == 'o':
            count2 += 1
        else :
            if count2 >= 5:
                return True
                break
            count2 = 0
        if count1 >= 5 or count2 >= 5:
            return True
    return False

#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result1 = rowcol(N, arr)
    result2 = cross(N, arr)

    if result1 or result2:
        print(f'#{tc} YES')
    else :
        print(f'#{tc} NO')




