import sys

sys.stdin = open('input1979.txt')
def row_count(N, K):
    total_count = 0
    for row in range(N):
        #        store_count = 0
        count = 0
        for col in range(N):
            if arr[row][col] == 1:
                count += 1
            #                store_count = count
            else:
                if count == K:
                    total_count += 1
                count = 0
        # 뒤에 만약에 count되었는데 합산이 total에 합산되지 않았을 경우 추가
        if count == K:
            total_count += 1
    return total_count

def col_count(N, K):
    total_count = 0
    for col in range(N):
        #        store_count = 0
        count = 0
        for row in range(N):
            if arr[row][col] == 1:
                count += 1
            #                store_count = count
            else:
                if count == K:
                    total_count += 1
                count = 0
        # 뒤에 만약에 count되었는데 합산이 total에 합산되지 않았을 경우 추가
        if count == K:
            total_count += 1
    return total_count

#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    row = row_count(N,K)
    col = col_count(N,K)
    result = row + col

    print(f'#{tc} {result}')

