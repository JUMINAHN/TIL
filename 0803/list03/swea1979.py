import sys

sys.stdin = open('input1979.txt')

def check_row(arr, count):
    total = 0
    for row in range(N):
        for d in arr[row]:
            if d == 1:
                plus += 1
            else :
                total += plus
                plus = 0
    if total == 3:
        count += 1
    return count

#열계산하는 방법 까먹음
def check_col(arr, count):
    total = 0
    for column in range(N) :
        plus = 0
        for row in range(N):
            if 1 == arr[row][column]:
                plus += 1
            else :
                total += plus
                plus = 0
    if total == 3:
        count += 1
    return count

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #찾는 길이의 개수

    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    #count 정렬..

    find_row = check_row(arr, count)
    find_col = check_col(arr, count)
    print(f'#{tc} {find_row + find_col}')