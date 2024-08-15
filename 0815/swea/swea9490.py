import sys

sys.stdin = open('input9490.txt')
#테스트 케이스 개수
#부등호 방향 잘보기

T = int(input())
for tc in range(1, T+1):
    #1. 델타 문제
    #2. 추가로 상하 좌우가 더 터지는 문제
    #3. N줄에 M개씩의 풍선 (N=행, M=열)
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] #풍선이 들어있는 모든 칸이 채워진 상태
    #이제 제일 큰 꽃가루의 합을 확인해야 함

    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]
    #제일 큰 꽃가루를 찾기 위해선 내부에서 순회를 해야 함
    max_sum = 0
    for row in range(N):
        for col in range(M):
            delta_sum = 0 #상하좌우의 합을 구한다.
            #주의할 것은 추가로 더 풍선이 터진다.
            for k in range(len(data_row)):
                for combo in range(1, arr[row][col]+1): #combo로 추가로 더 터지기 때문에 -> 기존 값을 1로 시작하고 combo만큼 더 터뜨림
                    move_row = row + data_row[k] * combo #새로운 이동
                    move_col = col + data_col[k] * combo

                    #범위를 초과하는지 확인
                    #이동하는 것이 아니라 주변 최대값을 확인하고 합산
                    if 0 <= move_row < N and 0 <= move_col < M:
                        delta_sum += arr[move_row][move_col]
            delta_sum += arr[row][col] #나의 값까지 더해줍니다.
            if max_sum < delta_sum:
                max_sum = delta_sum
    print(f'#{tc} {max_sum}')