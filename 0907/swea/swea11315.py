import sys

sys.stdin = open('input11315.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #N*N판
    omok = [list(input()) for _ in range(N)]

    #8방향 오목 보기
    #오목 자체가 같은 방향에 있는지를 비교하고자 하는 것
    #상하 / 좌우 / 왼->오 / 오->왼
    data_row = [[-1,1], [0,0], [-1, 1], [-1, 1]]
    data_col = [[0,0], [-1, 1], [-1, 1], [1, -1]]

    result = 'NO'
    for row in range(N):
        for col in range(N):
            if omok[row][col] == 'o':
                for d in range(len(data_row)): #첫번째 [-1, 1]을 추출할 것이고
                    find_sum = 0
                    for i in range(1, 3): #2개를 추가로 더 비교해야하는 상황이기 떄문에
                        for k in range(len(data_row[0])): #d만큼 돌면 상하 좌우 #-1, 1 만큼 돌고
                            move_row = row + data_row[d][k] * i#첫번째 d에 첫번쨰 k
                            move_col = col + data_col[d][k] * i #이동을 더하지 않았음.. -> 오타
                            #print(data_row[d])
                            if 0<=move_row<N and 0<=move_col < N and omok[move_row][move_col] == 'o': #이거일떄만 해당됨
                                find_sum += 1 #find섬에 개수만큼 더해진다.
                    #print(find_sum)
                    if find_sum >= 4: #자기는 일단 포함하지 않았음
                        result = 'YES'
                        break #for d에 있는 조건을 나가게 한다.
            if result == 'YES':
                break
        if result == 'YES':
            break
    print(f'#{tc} {result}')