# import sys
#
# sys.stdin = open('input2828.txt')
# #테스트 케이스 개수
# T = int(input())
# for tc in range(1, T+1):
N, M = map(int, input().split()) #스크린 N, 바구니 M
screen = [0] * (N+1) #스크린
#마지막에는 screen의 0번째 idx를 pop해줘야함, 1부터 시작하기 떄문에 ----------------------------------> 추후 점검


J = int(input()) #사과가 떨어지는 개수
apple_pos = [int(input()) for _ in range(J)] #1, 5, 3의 순서
left_idx = 1 #첫번째 idx위치
right_idx = M #마지막 idx위치 -> M만큼 차지하니까
apple_count = 1 #현재는 1 -> 2 -> 3 총 3번 카운트 되니까 해당 부분을 증가시켜준다.
move = 0
while apple_count <= J: #J가 되면 끝
    #현재 위치와 내가 찾는 apple의 위치가 같은지 확인
    #1. left idx가 screen의 1번에 닿이면 -> `right_idx`가 기준이 된다.
    if left_idx == 1:
        #첫번째 count와 right_idx가 같다면
        if apple_pos[apple_count-1] == right_idx: #오른쪽을 기준으로 확인
            apple_count += 1 #apple count를 올려줌 -> apple을 찾았다는 것
            continue #다시 while문으로 돌아가라
        else: #같지 않다면 -> 이전 위치에서 right_idx == 1, 현재 위치 apple pos == 5
            #prev = right_idx #이전 idx
            #잠깐 여기서 범위를 초과할 경우
            #distace = apple_pos[apple_count] - right_idx
            while right_idx < apple_pos[apple_count-1]: #idx자체가 N까지 가능 -> 해당 위치까지 증가
                move += 1
                right_idx += 1
                left_idx += 1
                #print('mv', move)
            apple_count += 1 #다 찾고 count -> 이걸 안해줌
            # if distace > N: #N을 초과할 경우 -> idx자체가 N을 초과할 경우 --> N+1까지니까 N까지 가능 -> 단 %범위는 N까지 -> 쉽게 확인하기 위해서 while로
            # right_idx = apple_pos[apple_count]
            # left_idx += distace #증가한만큼 더해주기
            # move += distace
            #현재에서 다음으로 이동하면 move += 이동한 만큼
    elif right_idx == N: #idx가 N+1만큼이니까 마지막 idx는 N
        # print('ac', apple_count)
        # print('mv', move)
        # print('r', right_idx)
        # print('l', left_idx)
        if apple_pos[apple_count-1] == left_idx: #오른쪽을 기준으로 확인
            apple_count += 1 #apple count를 올려줌 -> apple을 찾았다는 것
            continue #다시 while문으로 돌아가라
        else :
            while left_idx > apple_pos[apple_count-1]: #idx자체가 N까지 가능 -> 해당 위치까지 증가
                move += 1
                right_idx -= 1
                left_idx -= 1
                #print('mv', move)
            apple_count += 1 #이걸 안해줬음
print(move)

    #2. right idx가 screen의 마지막에 닿이면 -> 'left_idx`가 기준이 된다.