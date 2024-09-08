import sys

def change_stone(data):
    if data == 1:
        return 0
    else :
        return 1

sys.stdin = open('input20396.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())#돌의개수, 뒤집는 횟수
    stone = list(map(int, input().split())) #돌 초기값

    for _ in range(Q):
        I, J = map(int, input().split())
        I -= 1 #index위치 설정을 위해서
        first_color = 0
        for i in range(I, I+J):
            if i == I:
                first_color = stone[i]
            if 0<=i <N:
                stone[i] = first_color
            #print(first_color)
    #출력값 잘보기
    print(f'#{tc}', end= ' ')
    print(*stone)
    #print('-------')
    #print(stone)