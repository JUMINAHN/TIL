import sys

sys.stdin = open('input1220.txt')
#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    #교착상태가 무엇인진 모르겠고, 먼저 데이터에 있는 값들을 옮겨야 함
    N = int(input()) #테이블의 크기
    table = [list(map(int, input().split())) for _ in range(N)] #지금 테이블에 있는 것
    #일단 위가 N극 1 / 아래가 S극 2
    #여기서는 row는 필요없고, col로 이동을하게된다.
    #일단 그러면 한쪽row씩 자석으로 떙기자

    # N_idx = 0
    # S_idx = N-1
    # for i in range(N):
    #     while N_idx != S_idx:
    #         table[][i]
    # for col in range(N):
    #     for row in range(N):
    #         #만약 같을경우. .
    #         #N극 +1, S극 -1
    #         #n-1을 하는 이유는 99에서 +1을 하면 100이 되기 떄문에 마지막 idx 99임을 고려하여 98에서 멈추게 했다.
    #         if table[row][col] == 1 and 0<= row < N-1: #아래로 값을 옮겨준다 근데 범위가 벗어날수도 있으니까 여기 조건도 써준다.
    #             table[row+1][col], table[row][col] = table[row][col], table[row+1][col] #두개 값을 바꿔준다.
    #         if table[row][col] == 2 and 0<row<N: #0보다 작으면 안됨 0까지만 가능하기 떄문에
    #             table[row-1][col], table[row][col] = table[row][col], table[row-1][col]

    print(table)