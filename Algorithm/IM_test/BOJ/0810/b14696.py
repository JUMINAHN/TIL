#딱지놀이 우선순위 도출
round = int(input())
for tc in range(round):
    a_card = list(map(int, input().split()))
    b_card = list(map(int, input().split()))

    #받은 카드들에 1부터 4가 몇개인지 확인하기 -> 4가 우선순위임을 까먹지 말기 일단 count
    #보면 잘못 주는 카드 5가 있음 --> 여분으로 10까지 만들자
    #카드에 각 카드 개수를 살리기
    a_count = [0] * 10
    for a in a_card:
        a_count[a] +=1
    b_count = [0] * 10
    for b in b_card:
        b_count[b] += 1
    #print(a_count)
    #print(b_count)

    #우선순위 비교하기 먼저 지문에 있는 조건을 모두 만족할 때 -> 0이 없을 때 -> not in 0
    for i in range(4, 0, -1): #4번부터 우선순위 비교
        if a_count[i] > b_count[i]:
            print('A')
            break
        elif a_count[i] < b_count[i]:
            print('B')
            break
#            if a_count[i] == 0:
#                print('A')
#                break
#        else :

        else:
            if i == 1:
                print('D')

    #만약 i가 3번째 일 때 a의 길이가 더 짧다면, a가 이기는 것이고 --> 즉 a_count[3] not in 0이면, 그게 아니면 b
    #만약 i가 2번쨰 일 때 a의 길이가 더 짧다면, a가 이기는 것이고
    #만약 i가 1번쨰 일 때 a의 길이가 더 짧다면, a가 이기는 것

    #가장 좋은 것은 조건마다 내부의 길이를 비교해서 길이가 다르다면, 해당 조건을 만족하면 바로 출력하게 하고 싶음..

    # if a_count[1:5] not in 0 and b_count[1:5] not in 0: #이 케이스는 뭔가 일단 개수가 안맞으면 실행이 안됨-> 4번케이스의 경우 error발생 가능성
    #    for i in range(4, 0, -1): #4번부터 우선순위 비교
    #         if a_count[i] > b_count[i]:
    #             print('A')
    #         elif a_count[i] < b_count[i]:
    #             print('B')
    #         else:
    #             if i == 1:
    #                 print('D')
    #만약 이 상기 조건들이 만족이되지 않았다면

