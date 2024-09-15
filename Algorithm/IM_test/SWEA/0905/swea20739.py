import sys

sys.stdin = open('input20739.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split()) #사진 데이터를 담을 행 열
    pic = [list(map(int, input().split())) for _ in range(N)] #사진 데이터를 담음
    #1이 들어있으면 데이터가 있는 것
    #행/열 비교해야 함 -> 연속된 1의 개수와 동일

    #행 순회
    max_sum = 0
    for row in range(N):
        #먼저 열내부에서 값을 비교해줘야 함, 하나씩이니까
        row_sum = 0
        for col in range(M):
            if pic[row][col] == 1:
                row_sum += 1
                if max_sum < row_sum and row_sum > 1: #가장 높은 값 갱신하고 -> 구조물의 최소 크기는 2라서
                    max_sum = row_sum
            else :
                if max_sum < row_sum and row_sum > 1: #가장 높은 값 갱신하기
                    max_sum = row_sum
                row_sum = 0
    #열 순회
    for col in range(M):
        #먼저 열내부에서 값을 비교해줘야 함, 하나씩이니까
        col_sum = 0
        for row in range(N):
            if pic[row][col] == 1:
                col_sum += 1
                if max_sum < col_sum and col_sum > 1: #가장 높은 값 갱신하고 -> 구조물의 최소 크기는 2라서
                    max_sum = col_sum
            else :
                if max_sum < col_sum and col_sum > 1: #가장 높은 값 갱신하기
                    max_sum = col_sum
                col_sum = 0
    print(f'#{tc} {max_sum}')


