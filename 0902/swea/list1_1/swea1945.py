#import sys

#sys.stdin = open('input1945.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = b = c = d = e = 0

    while N != 1 :#1이 될때까지
        if N % 2 == 0:
            N = N // 2#N의 값을 바꿔주고
            a += 1
        elif N % 3 == 0:
            N = N // 3
            b += 1
        elif N % 5 == 0:
            N = N // 5
            c += 1
        elif N % 7 == 0:
            N = N // 7
            d += 1
        elif N % 11 == 0: #오탈자 유의
            N = N // 11
            e += 1
    print(f'#{tc} {a} {b} {c} {d} {e}')


