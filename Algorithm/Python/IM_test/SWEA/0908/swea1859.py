import sys

sys.stdin = open('input1859.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #1. 최대한 많은 이익 -> `최대` == 욕심 == 그리디
    #2. 연속 N일 동안 매매가 예측 가능
    N = int(input())
    #3. 언제든지 판매 가능 -> 나의 마음대로
    price = list(map(int, input().split()))

    # 1.뒤에서 부터 접근한다. == 가장 큰 값을 담기 위해 Max_profit에 N-1값을 담아준다.
    Max_price = price[-1] #가장 큰 값을 담는다.
    # 이익을 계산할 변수 선언
    profit = 0
    #일단 해당 idx니까 뺼 것은 없다.
    now = 0
    prev = 0 #idx들을 담는다.
    for i in range(N-1, 0, -1) : #뒤에서 부터 접근 조금 덜 해도 된다.
        #print(i)
        now = i
        # prev = i-1 #어제 값
        #print(prev)
    # 2. 오늘 > 어제라면, 오늘 Data 즉 Max_profit을 기반으로 뺴준다.
        if price[now] < Max_price : #max_pirce에서 금일 '오늘'이 아닌 `어제` # 가격을 뺴준다. -> now -> 같거나 같으면.. 동일 적용
            profit += Max_price - price[now] #왜냐하면 일단 오늘의 값은 똑같을 것이니까
            #print(profit)
    # 3. 오늘 < 어제 : 그러면 오늘 판매한다. -> 그리고 어제를 Max_profit으로 담아준다.
        else: #그게 아니라면 now < prev 라면? -> 사지 않는다는 전제조건이 필요없으니까 판매한다. 즉 Max_profit을
            #어제 뺏을거니까 단순 갱신
            Max_price = price[now] #어제 가격 #갱신이 안된듯?
            #print(Max_price)

    #마지막 가격이 들어갔는지 확인
    print(f'#{tc} {profit}')

#가격을 비교할 때 price[now]와 price[prev]를 비교하는 것이 아니라, 가격이 더 높은 Max_price와 비교하는 것이 더 적절

'''
1. 최대한 많은 이익 -> `최대` == 욕심 == 그리디
2. 연속 N일 동안 매매가 예측 가능
3. 언제든지 판매 가능 -> 나의 마음대로

#1.뒤에서 부터 접근한다. == 가장 큰 값을 담기 위해 Max_profit에 N-1값을 담아준다.
#2. 오늘 > 어제라면, 오늘 Data 즉 Max_profit을 기반으로 뺴준다.
#3. 오늘 < 어제 : 그러면 오늘 판매한다. -> 그리고 어제를 Max_profit으로 담아준다.
'''