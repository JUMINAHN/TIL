import sys

sys.stdin = open('../input1859.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #1. N : 일수
    N = int(input())
    #2. 매매가를 나타내는 자연수 여러개
    sales = list(map(int, input().split()))

    #문제 조건
    #아무래도 모든 케이스를 검증해야하고, 일수가 정해져있으니까 반복문 = for를 사용하면 되지 않을까?
    #코드를 작성하다 보니 now, prev를 계속 바꿔줘야하기 떄문에.. while을 쓰는게 더 편리할 수도

    prev = sales[0] #지금
    now = sales[1] #그다음 -> 초기세팅으로 일단 넣는다.
    now_idx = 1 #setting
    #이익 count
    profit = 0
    #합산 이익
    total_profit = 0

    while now_idx != N-1: #조건이 성립되면 out
        # 1.현재 i보다 다음 i(내일)이 작으면 -> 어제가 더 크면 지금이 더 작으면 0의 이익을 가진다.
        if now < prev:
            total_profit += profit #계속 합산되기 떄문에
            # 지금 data를 prev에, 다음 data를 now에 넣는 형식
            # 즉 해당 케이스의 경우 이익 합산값을 초기화 하고 다시 0 or n부터 다시 산정한다.
            profit = 0
        else : #now가 이전보다 클 경우 -> 이익을 산정해주는 케이스
            # 2. 그 반대로 현재 i보다 다음 i(내일)이 크면, 내일 - 현재를 이익으로 둔다
            #print('now', now)
            #print('prev', prev)
            new_profit = now - prev
            profit += (total_profit + new_profit) #이런식으로 누적이 된다.
            total_profit += profit
            #print(profit)

            # 단, 누적합으로 진행된다.
            # 이전 합산 값이 2이고, 현재가 4라면 2에 2+4를 더해진 값을 얻는다.
            # 접근 방법 생각해보기
        #상기 행위가 끝나면 하기는 공통적으로 진행되는 것들
        prev = now
        now = sales[now_idx + 1]  # 현재idx 다음 , 실제 now도 증가시켜주고    #'int' object is not subscriptable
        now_idx += 1  # 나우 idx증가시켜주고

    print(total_profit)

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