#우선순위를 먼저 비교하는 것부터 시작한다. --> 이거 일단 참고
#N = 라운드수 input받고
#2번째, 3번째에는 a/b의 card정보를 받는다 --> 이 부분들이 반복 순회된다.
#여기서 키포인트는 a와 b카드의 1~4까지를 count정렬을 통해 count해서 개수를 확인하고
#우선순위를 기준으로 조건을 나누어 접근해야 한다.
N = int(input())
for tc in range(N):
    a_card = list(map(int, input().split()))
    b_card = list(map(int, input().split()))
    #각 내용을 count정렬로 비교합니다. --> count에 각각의 idx가 담을 수 있도록 그럼 즉 count의 1번만 수행
    #카드는 4개의 모양 -> 즉 종류 4개다.
    #근데 지금 testcase를 보면 5번까지 있다.. 뭐지..? --> 없는 카드를 꺼냇을경우라고 생각을 해보고 범위를 더 높게 잡자
    count_a = [0] * 10 #주의해야할 것은 0번은 사용하지 않기 떄문에 종류 + 1을 해줘야 한다.
    count_b = [0] * 10
    for a in a_card:
        count_a[a] += 1
    for b in b_card:
        count_b[b] += 1
    #print(count_a)
    #print(count_b)
    #우선순위가 더많은 경우 이긴다. 1부터 4까지만 하면 된다.
    #별의 개수가 같고 동그라미의 개수가 다르다면, 동그라미가 많은 쪽의 딱지가 이긴다.

    #다 똑같은 카드의 개수가 전재라면
    if count_a in (1,2,3,4) and count_b in (1,2,3,4):
        for i in range(4,0,-1):
            if count_a[i] > count_b[i]:
                print('A')
                break
            elif count_a[i] < count_b[i]:
                print('B')
                break
            else: #둘다 같다면
                if i == 1: #맨 마지막의 케이스 까지 모두 돌 때
                    print('D')
                    break
    #카드의 개수가 더 작은 경우는 더 작은 쪽이 출력됨 -> LEN을 할려니까 0이 있어서 소용없을 것 같음
    elif len(count_a[1:5]) > len(count_b[1:5]):
        if count_a[4] > count_b[4]:
            print('A')
#    elif len(count_a[1:5]) < len(count_b[1:5]):
#        if count_a[4] < count_b[4]:
#            print('B')
#    else:
#        if count_a[4] > count_b[4]:
#            print('A')
#        else:
#           print('B')
#        #별이 많으면 이긴다.
