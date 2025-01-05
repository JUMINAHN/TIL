#N*M의 풍선에 들어있는 꽃가루 개수 A, 한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 최대값을 출력
#NxM개의 풍선에 들어있는
import sys

sys.stdin = open('input16268.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] #N만큼 반복해야 함

    total_max = 0
    #델타 탐색 -> 상하좌우방문
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]
    for row in range(N):
        for col in range(M):
            total_sum = 0
            for k in range(len(data_row)): #4방향을 돌것이기 때문에
                move_row = row + data_row[k]
                move_col = col + data_col[k]

                if 0<=move_row<N and 0<= move_col<M : #그냥 상하좌우
                    total_sum += arr[move_row][move_col]
            total_sum += arr[row][col]
            if total_max < total_sum :
                total_max = total_sum
    print(f'#{tc} {total_max}')
