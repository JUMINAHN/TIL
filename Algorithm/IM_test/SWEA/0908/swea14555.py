import sys

sys.stdin = open('input14555.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    yeild = list(input())
    #print(yeild)
    prev = yeild[0]
    ball = 0
    for i in range(1, len(yeild)):
        prev = yeild[i-1]
        now = yeild[i]
        if prev == '(':
            if now == ')':
                ball+= 1
            elif now == '|':
                ball += 1
        elif prev == '|':
            if now == ')':
                ball += 1
    print(f'#{tc} {ball}')
