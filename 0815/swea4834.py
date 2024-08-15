import sys

sys.stdin = open('input4834.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #가장 많은 카드에 적힌숫자와 카드가 몇장인지? -> 카드 장수가 같을땐 적힌 숫자가 큰 쪽
    #적힌 숫자가 큰쪽이라는 것은 같거나, 크면 됨 -> 같을 경우 새로운 값이 덮어쓰이기 때문에
    #카드 장수 N
    N = int(input())
    #카드 장수의 번호가 적힌것 N개만큼
    num_list = list(map(int, input())) #split안해도 -> 4 9 6 7 9 처럼 들어갈 것
    #가장 많이 적힌 숫자와 카드가 몇 장인지
    #0부터 9사이의 카드가 여백없이 주어지는 것
    count = [0] * 10 #총 10장 -> 0부터 9까지
    for num in num_list:
        count[num] += 1 #해당 되는 것들 증가

    #가장 많이 적힌 숫자와 그 카드가 몇 장인지
    #count된 것 중에 max, 그리고 idx! --> 한꺼번에 보려면
    max_num = 0 #count된 것
    max_idx = 0

#    print(count[0])
    for i in range(len(count)): #10까지 -> idx 0부터 9까지 : 따라서 N만큼이 아니라 카운트만큼 세야해
        #numlist의 내부 자체에서 값을 구하는 것이 아니라 내가 counting한 -> 세고 싶은 값에서 시작
        if max_num <= count[i]:  #'<' not supported between instances of 'list' and 'int'
            max_num = count[i] #위에선 비교가 되었지만 max_num에서 오류가 발생
            max_idx = i
    print(f'#{tc} {max_idx} {max_num}')