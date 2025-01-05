import sys

sys.stdin = open('input1217.txt')
#테스트 케이스 개수
T = 10

def zecop(N, M): #M이 8을 받으면 0~7번까지
    if M == 0:
        return 1 #마지막에는 1을 돌려준다.
    M -= 1
    return N * zecop(N,M)



for tc in range(1, T+1):
    test_case = int(input())
    N, M = map(int, input().split()) #9 8
    result = zecop(N,M)
    print(f'#{tc} {result}')
