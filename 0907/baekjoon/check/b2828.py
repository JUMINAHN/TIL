import sys
#사과 담기 게임
sys.stdin = open('../input2828.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #스크린 크기 N*N, 바구니 크기 M
    N, M = map(int, input().split())
    #모든것은 1부터 10까지 시작한다. -> 편의를 위해서 [0]을 하나 더 추가하고, index를 맞춰준다 -> 즉 N+1 해당 부분 유의하기
    screen = [0] * (N+1) #index를 맞추기위해서 -> 1번쨰 idx는 사용하지 않을 것
    J = int(input())#사과의 개수 -> 사과의 개수만큼 반복을 해야한다.
    #모든 사과를 담고, 이동 거리를 최소화하려고 한다.
    apple_pos = [int(input()) for _ in range(J)]
    #print(apple_pos)
    #현재 index를 설정한다.
    #left = 1, right = 1+M-1로 둔다. -> 초기 세팅의 idx가 1번임
    left_idx = 1
    right_idx = 1+M-1 #즉 M
    move_count = 0
    apple_count = 1
    #apple pos만큼 돈다.
    #횟수를 모르니까 while로 둔다.

    while apple_count <= J: #총3개 #1부터 시작해 -> 근데 idx는 0부터 접근해야 함
        if left_idx == apple_pos[apple_count] or right_idx == apple_pos[apple_count]:
            apple_count += 1 #apple count를 올려준다 찾았으니까
        #같지 않을 경우 -> 일단 ->로 가는 방향 먼저 고려
        # 1. 지금 < 다음:
        elif right_idx <= N: #N까지 가능하니까
            pass
        # right_idx 즉 오른쪽을 기준으로 idx를 증가시킨다.
        # left_idx도 right_idx만큼 증가되어야 한다.
        # 2. 지금 > 다음 :
        # left_idx 즉 왼쪽을 기준으로 idx를 감소시킨다.
        # right_idx도 left_idx만큼 감소되어야 한다.




    #     pos = int(input())
    #     if left_idx == pos or right_idx == pos:
    #         apple_count += 1 #찾았으니까 apple_count를 증가시킨다.
    #         prev = pos #아까의 pos를 넣어준다.


    #오른쪽과, 왼쪽을 기준으로 나눈다.




    '''
        #횟수를 모르니까 while로 둔다.
    #left = 1, right = 1+M-1로 둔다. -> 초기 세팅의 idx가 1번임
    #오른쪽과, 왼쪽을 기준으로 나눈다.
    #1. 지금 < 다음:
        #right_idx 즉 오른쪽을 기준으로 idx를 증가시킨다.
            #left_idx도 right_idx만큼 증가되어야 한다.
    #2. 지금 > 다음 :
        #left_idx 즉 왼쪽을 기준으로 idx를 감소시킨다.
            #right_idx도 left_idx만큼 감소되어야 한다.
    '''