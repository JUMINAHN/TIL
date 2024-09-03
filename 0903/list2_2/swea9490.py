import sys

sys.stdin = open('input9490.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #안에 든 꽃가루 개수만큼 상하좌우가 추가로 터진다.
    #N*M안에 들어있는 꽃가루 개수 A
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #풍선팡 시작

    max_total = 0
    #범위만큼 돌 것
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]
    for row in range(N):
        for col in range(M):
            #하나의 범위에 대한 합산 값이 필요
            sum = 0
            s = arr[row][col]
            sum += s
            for i in range(1, s+1): #i만큼 더 .. 추가로 터뜨려야함
                for k in range(len(data_row)):
                    move_row = row + (data_row[k] * i)
                    move_col = col + (data_col[k] * i)
                    if 0<=move_row<N and 0<=move_col<M:#범위를 벗어나지 않게하기 위해서
                        sum += arr[move_row][move_col]
            if max_total < sum:
                max_total = sum
    print(f'#{tc} {max_total}')