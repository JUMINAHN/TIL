#import sys
#sys.stdin = open('input1979.txt')

#행 먼저 체크
def row_check(N, arr):
    total = 0
    for row in range(N):
        check_length = 0
        for col in range(N):
            if arr[row][col] == 1:
                check_length += 1
            else :
                if check_length == K:
                    total += 1
                check_length = 0
        if check_length == K:
            total += 1
    return total

#열먼저 체크
def col_check(N, arr):
    total = 0
    for col in range(N):
        check_length = 0
        for row in range(N):
            if arr[row][col] == 1:
                check_length += 1
            else :
                if check_length == K:
                    total += 1
                check_length = 0
        if check_length == K:
            total += 1
    return total

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] #단어가 있는 것을 확인할 수 있음
    row = row_check(N,arr)
    col = col_check(N,arr)

    print(f'#{tc} {row+col}')