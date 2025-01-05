import sys

sys.stdin = open('input3499.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #카드 장수
    card = list(input().split())
    if N % 2 == 1:
        front_c = card[:N//2+1]
        back_c = card[N//2+1:]
    else :
        front_c = card[:N//2]
        back_c = card[N//2:]
    #맞게 들어간 것 확인
    #print(front_c)
    #print(back_c)
    print(f'#{tc}', end=' ')
    #한개씩 출력
    for i in range(N//2): #그리고 나머지는 하나 걍 더 붙이자
        print(front_c[i], end = ' ')
        print(back_c[i], end = ' ')
    if N % 2 == 1:
        print(front_c[N//2], end = '') #맨 마지막 내용
    print()
