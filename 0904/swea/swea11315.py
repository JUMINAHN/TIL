import sys

sys.stdin = open('input11315.txt')
#테스트 케이스 개수
T = int(input())#testcase
for tc in range(1, T+1):
    #N*N의 돌이 들어있는 오목배열 (N은 5부터 20까지 가능), `o`는 돌이 있는 것
    N = int(input())#배열의 크기
    omok = [list(input()) for _ in range(N)] #오목이 들어있는 배열칸을 받는다
    #상하/좌우/대각선1/2을 순회해야함
    #묶어주자 -> 그냥 data_row자체로
    #대각선 1은 : 왼 -> 오, 대각선 2는 : 오 -> 왼
    data_row = [[-1, 1], [0, 0], [-1, 1], [-1, 1]]
    data_col= [[0, 0], [-1, 1], [-1, 1], [1, -1]]
    # 2-1. 주변 탐색은 상하/ 좌우/ 대각선1 / 대각선2를 세트로 구별한다

    #1. 일단 전체를 순회한다. for row , col로 row를 그대로 유지하면 됨
    result = 'NO'
    for row in range(N):
        for col in range(N):
            # 2. 전체를 순회하다가 if == 'o'를 만나게되 면, 주변을 탐색한다
            if omok[row][col] == 'o': #얘를 만나게 되면 시작을 한다.
                for d in range(len(data_row)): #상하 / 좌우 / 왼오 / 오왼
                    #그리고 k만큼 이동을 한다.
                    #나까지 추가를 해줘야할까? -> 근데 자체적으로 내가 o야 진행을 할 수 있도록 코드를 짯는데..
                    inner_total = 1 #inner에 계산을 한다. 개수 확인을 위해서
                    for k in range(len(data_row[0])): #일단 0번쨰를 기준으로
                        for i in range(1, 3): #왜냐면 오목의 2칸까지 점검해야 하기 떄문에
                            # 세트로 상하를 구분하는 이유는 나보다 위에 2칸, 아래에 2칸이 모두 있을 경우 오목의 1줄이 완성되기 떄문에
                            # 2-2.따라서 나를 제외하고 set로 위에 2칸, 아래에 두칸 이상씩 있으면 성립이된다.
                            move_row = row + (data_row[d][k] * i) #얘를 들면 첫번쨰 data_row의 첫번째 k를 구하는 것
                            move_col = col + (data_col[d][k] * i)
                            if 0<=move_row<N and 0<=move_col<N and omok[move_row][move_col] == 'o': #오목이 있을 때 -> 오탈자
                                inner_total += 1
                    # 2-3따라서 if sum >= 4보다 크다면 Yes값을 return 출력을 하면 되고,
                    if inner_total >= 5: #나를 제외하고 추가로 더 있다고 가정했을 때 #5로 설정하니까 무한루프를 도는 이유..?
                        result = 'YES' #결과값을 바꿔준다.
                        #break
                    #2-3-1. 만약 sum보다 작다면 그냥 다시 한 번 더 순회를 하면 된다.
    print(f'#{tc} {result}')