import sys

sys.stdin = open('input16268.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #생긴것 == 델타로 접근한다.
    #가운데를 터트리면, 상하좌우가 추가로 1개씩 터진다. => 즉 나 자신과, 이동하는 칸 모두 커진다.
    #꽃가루의 최대값을 구하라 -> 합산의 최대값 (즉 arr[row][col] + 델타)
    #N은 행 M은 열
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] #델타로 접근할 이차원 리스트 생성
    #델타로 접근할 방향 생성
    #이동하는것이 아니니까 for문으로 돌려도 됨
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]

    #델타들과 나의 최대값을 담을 변수 생성
    max_delta = 0
    #각 열,행 즉 좌표값 (0,0)에 도착해서 나 자신과 내 주변요소들을 비교하면 됨
    #따라서 모든 2차원리스트를 순회하는 for문 생성
    for row in range(N):
        max_sum = 0 #하나를 순회하면서 비교할 결과, (1,1)일때 비교 (1,2)일떄 비교 따라서 col에 넣는다. -> 헷갈렸음
        for col in range(M):
            #arr[row][col]
            #방향전환까지 고려해야하기 때문에 방향전환과 관련된 for문을 생성
            #그렇다면 상하좌우를 모두 더할 값을 만들어줘야함
            rdlu = 0 #right down left up의 총 합 값
            for k in range(len(data_row)):
                move_row = row + data_row[k]
                move_col = col + data_col[k]
                #이 좌표가 arr의 배열 범위를 벗어나는지 확인해야 함
                if 0 <= move_row < N and 0 <= move_col < M:
                    rdlu += arr[move_row][move_col] #moverow와 movecol에 있는 내부 값에 접근 가능
            rdlu += arr[row][col] #나의 값을 더해줘야 함 (이동한 것과 나)
            #col을 순회한 것 중에 내가 크다면 max sum에 해당 됨
            if max_sum < rdlu :
                max_sum = rdlu
        if max_delta < max_sum :
            max_delta = max_sum
    print(f'#{tc} {max_delta}')
