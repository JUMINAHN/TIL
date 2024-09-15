import sys

sys.stdin = open('input12712.txt')

def nozzle(pari, N, M, data_row, data_col): #N과 M이 무엇을하는지 명확하게 기재하고 거기에 대한 정답값을 도출하자
    max_sum = 0
    for row in range(N):
        for col in range(N):
            delta_sum = 0
            #M크기 만큼의 노즐을 분사한다.
            for k in range(len(data_row)):
                for i in range(1, M) :#M이 주어졌을 떄 M-1개까지 넣어야함
                    move_row = row + data_row[k] * i
                    move_col = col + data_col[k] * i

                    #k의 범위를 벗어나는지 아닌지 확인하기
                    if 0<=move_row<N and 0<=move_col<N:
                        delta_sum += pari[move_row][move_col]
            delta_sum += pari[row][col] #가운데 노즐인 나를 추가
            if max_sum < delta_sum :
                max_sum = delta_sum
    return max_sum


#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #N은 N*N 즉 파리 개체수가 들어있는 칸, M은 세기(스프레이 분사) -> 실제는 가운데 제외 M-1만큼
    #파리의 개체수를 확인했다.
    #이제 모든 파리의 개체수를 돌면서 스프레이를 분사했을 때 얼만큼 죽을 수 있을지를 판별한다.
    N, M = map(int, input().split())
    pari = [list(map(int, input().split())) for _ in range(N)] #배열의 크기
    data_row1 = [0, 1, 0, -1]
    data_col1 = [1, 0, -1, 0]
    plus_sum = nozzle(pari, N, M, data_row1, data_col1)

    data_row2 = [-1, 1, 1, -1]
    data_col2 = [1, 1, -1, -1]
    cross_sum = nozzle(pari, N , M, data_row2, data_col2)

    if plus_sum > cross_sum:
        print(f'#{tc} {plus_sum}')
    else :
        print(f'#{tc} {cross_sum}')

