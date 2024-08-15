import sys

def find_start(ladder, N):
    start_row = 0
    start_col = 0
    for row in range(N):
        for col in range(N):
            if ladder[row][col] == 2:
                start_row = row
                start_col = col
                break
    return start_row, start_col

sys.stdin = open('input1210.txt')
#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    test_case = int(input())
    #평면상의 사다리는 1로 표현되고 도착지점은 2로 표현된다. 0은 갈 수 없는 곳
    #100*100의 2차원 배열로 주어진다. 즉 [0] ~ [99] 총 100개인 셈
    #출발점 x를 반환하는 코드 작성_출발 idx 확인
    #역순접근 row를 역순으로 접근하면 됨
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)]
    #채우는게 아니라 이동하는 것이라서 delta처럼 접근하되, for 구문을 사용하지 않는 것을 추천한다.
    #출발 row, col의 idx는 먼저 arr[row][col]의 위치를 확인해야 할 수 있을 것 같다.

    row,col = find_start(ladder, N) #start 지점 확인   # cannot unpack non-iterable NoneType object
    #print(row,col) #99, 57

    #row는 위로만 가면되고, col은 좌우로, 왔던 길을 다시 돌아가지 않기 위해서는 1을 0으로 바꿔주면 돌아갈일이 없다.
    #위가 우선이 아니라 왼쪽이 우선이어야 함
    #오/왼/위가 되어야 함
    data_row = [0, 0, -1]
    data_col = [1, -1, 0] #일단 그림으로 봤을떄 왼쪽 우선으로 잡았다.
    #언제까지 반복하나? row가 0일때까지

#    direction = 0 #방향은 먼저 0이다.
    #똑같은게 반복되니까 이걸 해결할 수 있도록
    while row != 0:
        for k in range(len(data_row)):
            ladder[row][col] = 0
            move_row = row + data_row[k]
            move_col = col + data_col[k]

            if 0<=move_row<N and 0<=move_col<N and ladder[move_row][move_col] != 0:
                row = move_row
                col = move_col

    print(f'#{tc} {col}')