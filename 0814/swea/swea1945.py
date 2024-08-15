import sys

sys.stdin = open('input1945.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    a = b = c = d = e = 0
    #조건문을 쓰기엔 애매하다 N%2가 0인것을 구하는게 아니라 --> 소인수 분해되는 것...
    #if N % 2 == 0이면 --> 25%2가 0이되지 않잖아..
    #조건을 뭐라고 쓰면 좋을까
    #나머지가 0일 수가 없는게 0이면 값이 붕 떠요
    while N != 1:
        if N % 2 == 0:
            N //= 2
            a += 1 # 한번씩 강제로 돌리기
        elif N % 3 == 0:
            N //= 3
            b += 1
        elif N % 5 == 0:
            N //= 5
            c += 1
        elif N % 7 == 0:
            N //= 7
            d += 1
        elif N % 11 == 0 :
            N //= 11
            e += 1

    print(f'#{tc} {a} {b} {c} {d} {e}')