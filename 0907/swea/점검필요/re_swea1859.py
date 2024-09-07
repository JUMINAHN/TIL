import sys

sys.stdin = open('../input1859.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #1. N : 일수
    N = int(input())
    #2. 매매가를 나타내는 자연수 여러개
    sales = list(map(int, input().split()))

    '마지막 날에 팔면 3의 이익을 얻을 수 있다.'
    prev = sales[N-2]
    now = sales[N-1] #일단 설정
    profit = 0
    total_profit = 0
    for i in range(N-1, 0, -1): #뒤에서부터 접근한다.
        if now < prev:
            profit = 0 #그냥 이게 0인 것
            break
        else: #그게 아니라면
            profit = now - prev #예를들면 9-5
            #print(profit)
            total_profit += profit
        #now값이 갱신이 되지 않고 있음
        now = sales[i]
        prev = sales[i-1]
#        print(total_profit)
    #print(total_profit)

    # 1.현재 i보다 다음 i(내일)이 작으면 0의 이익을 가진다.
    # 지금 data를 prev에, 다음 data를 now에 넣는 형식
    # 즉 해당 케이스의 경우 이익 합산값을 초기화 하고 다시 0 or n부터 다시 산정한다.

    # 2. 그 반대로 현재 i보다 다음 i(내일)이 크면, 내일 - 현재를 이익으로 둔다
    # 단, 누적합으로 진행된다.
    # 이전 합산 값이 2이고, 현재가 4라면 2에 2+4를 더해진 값을 얻는다.
    # 접근 방법 생각해보기


    '''
    #문제 조건
    #1.현재 i보다 다음 i(내일)이 작으면 0의 이익을 가진다.
        # 지금 data를 prev에, 다음 data를 now에 넣는 형식
        # 즉 해당 케이스의 경우 이익 합산값을 초기화 하고 다시 0 or n부터 다시 산정한다.
    
    #2. 그 반대로 현재 i보다 다음 i(내일)이 크면, 내일 - 현재를 이익으로 둔다
        #단, 누적합으로 진행된다.
            #이전 합산 값이 2이고, 현재가 4라면 2에 2+4를 더해진 값을 얻는다.
                #접근 방법 생각해보기 
    '''


    #1번 케이스 과거 데이터

    # for i in range(1, N): #현재와 어제를 비교한다 -> 상기와 약간 다른
    #     now = sales[i] #1부터 시작하기 떄문에
    #     if now < prev:
    #         profit = 0
    #         now =