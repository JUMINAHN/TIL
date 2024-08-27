import sys

sys.stdin = open('input9489.txt')

def find_row(N, M):
    row_max_length = 0

    #row 기준으로 먼저 탐색
    for row in range(N):
        store = 0 #행마다 보관할 보관소
        row_count = 0 #count할 count함
        for col in range(M):
            if arr[row][col] == 1:
                row_count += 1
                if store < row_count:
                    store = row_count
                #여기 있는 친구가 최종적으로 count가 안되어 있을 수도 있음
                #store = row_count를 해야할지 - keeping
            else :
                row_count = 0
        if row_max_length < store:
            row_max_length = store
    return row_max_length


def find_col(N, M):
    col_max_length = 0

    # row 기준으로 먼저 탐색
    for col in range(M):
        store = 0  # 행마다 보관할 보관소
        col_count = 0  # count할 count함
        for row in range(N):
            if arr[row][col] == 1:
                col_count += 1
                if store < col_count: #무작정 대입하는게 아니라 클 경우만 그대로 대입하도록
                    store = col_count
                # 여기 있는 친구가 최종적으로 count가 안되어 있을 수도 있음
                # store = row_count를 해야할지 - keeping
            else:
                col_count = 0
        if col_max_length < store:
            col_max_length = store
    return col_max_length

#테스트 케이스 개수
T = int(input()) #input : 3
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range (N)] # 고대 유적이 박혀있는 것 확인 가능
    count_row = find_row(N, M)
    count_col = find_col(N, M)
    if count_row > count_col :
        print(f'#{tc} {count_row}')
    else :
        print(f'#{tc} {count_col}')



