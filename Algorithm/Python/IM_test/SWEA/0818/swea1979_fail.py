import sys

sys.stdin = open('input1979.txt')

# 행 계산
def check_row(puzzle, N, K):
    total_K = 0
    for row in range(N):
        # 한 행마다 해당 되는 값을 비교해야하기 때문에
        max_K = 0  # max_K 즉, k가 몇번 카운팅되는지 전체에 반영하기 위한 변수명
        count_K = 0  # k가 몇번 카운팅되는지 확인하기 위한 변수명
        for col in range(N):
            if puzzle[row][col] == 1:
                count_K += 1
            else:  # 퍼즐이 만약 1이 아니라면, 현재의 count값을 비교해서 전체에 반영하기 위한 변수명에 할당
                max_K = count_K  # 현재 카운팅된 것을 max_K에 전달
                count_K = 0  # count K 초기화
                
        # 순회를 하고 마지막 값이 1일 경우 max_K에 저장이 되지 않은 경우가 발생하기 떄문에 해당 부분 다시 진행
        # max_K = count_K #현재의 카운트를 total에 반영할 count에 전달
        # 위의 주석 역할으 처리하긴 해야하는데 일단 현재 count가 3이상이면 -> 3이면 max_count에 반영
        if count_K >= K:
            max_K = count_K
        if max_K == K:  # max_K가 3이면 total에 반영
            total_K += 1
    return total_K

# 열 계산
def check_col(puzzle, N, K):
    total_K = 0
    for row in range(N):
        # 한 행마다 해당 되는 값을 비교해야하기 때문에
        max_K = 0  # max_K 즉, k가 몇번 카운팅되는지 전체에 반영하기 위한 변수명
        count_K = 0  # k가 몇번 카운팅되는지 확인하기 위한 변수명
        for col in range(N):
            if puzzle[col][row] == 1:
                count_K += 1
            else:  # 퍼즐이 만약 1이 아니라면, 현재의 count값을 비교해서 전체에 반영하기 위한 변수명에 할당
                max_K = count_K  # 현재 카운팅된 것을 max_K에 전달
                count_K = 0  # count K 초기화
        # 순회를 하고 마지막 값이 1일 경우 max_K에 저장이 되지 않은 경우가 발생하기 떄문에 해당 부분 다시 진행
        # max_K = count_K #현재의 카운트를 total에 반영할 count에 전달
        # 위의 주석 역할으 처리하긴 해야하는데 일단 현재 count가 3이상이면 -> 3이면 max_count에 반영
        if count_K >= K:
            max_K = count_K
        if max_K == K:  # max_K가 3이면 total에 반영
            total_K += 1
    return total_K

#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) #가로/세로 N, 단어의 길이 K
    #퍼즐 생성
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    #전체 퍼즐을 순회하면서 해당되는 값이 있는지 확인
    total_row = check_row(puzzle, N, K)
    #현재 col이 문제임을 확인할 수 있음

    #total_col = check_col(puzzle, N, K)
    result = total_row # + total_col
    print(f'#{tc} {result}')



