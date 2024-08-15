import sys

sys.stdin = open('input1979.txt')
#테스트 케이스 개수
#sum값 고정으로 오류가 발생
#행우선, 열기준 -> 내용을 바꿀거면 위치만 바꿔주면 됨
def check_row(puzzle, N, K):
    col_total = 0
    for row in range(N):
        sum = 0
        for col in range(N): #col 값
            if puzzle[row][col] == 1:
                sum += 1 #1이 발견되면 연속성을 계속 더할 것이고
                #그런데 마지막 1이 sum으로 끝나면 해당 부분은 반영이 되지 않는다.
            else :
                if sum == K: #전체연속더해지는게 3이면
                    col_total += 1 #col total에 플러스 +1
                sum = 0 #그게 아니라면 sum을 초기화할 것이다.
        if sum == K:  #마지막 한 번 더 해주는 이유는 sum에 +1을 한 것으로 끝낫을 떄 col total에 반영이 되지 않기 떄문이다.
            col_total += 1  # col total에 플러스 +1
    return col_total

def check_col(puzzle, N, K):
    row_total = 0
    for row in range(N):
        sum = 0
        for col in range(N): #col 값
            if puzzle[col][row] == 1:
                sum += 1 #1이 발견되면 연속성을 계속 더할 것이고
                #그런데 마지막 1이 sum으로 끝나면 해당 부분은 반영이 되지 않는다.
            else :
                if sum == K: #전체연속더해지는게 3이면
                    row_total += 1 #col total에 플러스 +1
                sum = 0 #그게 아니라면 sum을 초기화할 것이다.
        if sum == K:  #마지막 한 번 더 해주는 이유는 sum에 +1을 한 것으로 끝낫을 떄 col total에 반영이 되지 않기 떄문이다.
            row_total += 1  # col total에 플러스 +1
    return row_total

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) #가로세로길이 N, 단어길이 K
    puzzle = [list(map(int, input().split())) for _ in range(N)] #puzzle에 값을 채워넣기
    col_total = check_row(puzzle, N, K)
    row_total = check_col(puzzle, N, K) #점검 필요
    print(f'#{tc} {col_total + row_total}')
    #testcase 4번은 0이 나와야 하는데,,
    #testcase 6번도 2가 나와야 하고
    #testcase 8번도 0이 나와야 하고
    #testcase 10번도 7이 나와야 한다.

    #loop를 통해 모든 좌표에 접근하여서 1의 유무를 확인할 것

    # col_total = 0
    # for row in range(N):
    #     sum = 0
    #     for col in range(N): #col 값
    #         if puzzle[row][col] == 1:
    #             sum += 1 #1이 발견되면 연속성을 계속 더할 것이고
    #             #그런데 마지막 1이 sum으로 끝나면 해당 부분은 반영이 되지 않는다.
    #         else :
    #             if sum == 3: #전체연속더해지는게 3이면
    #                 col_total += 1 #col total에 플러스 +1
    #             sum = 0 #그게 아니라면 sum을 초기화할 것이다.
    #     if sum == 3:  #마지막 한 번 더 해주는 이유는 sum에 +1을 한 것으로 끝낫을 떄 col total에 반영이 되지 않기 떄문이다.
    #         col_total += 1  # col total에 플러스 +1

