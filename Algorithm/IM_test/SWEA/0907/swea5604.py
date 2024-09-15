import sys

sys.stdin = open('input5604.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #8부터 12의 구간합은 8 + 9 + 10 + 11 + 12인데 -> 10의 자리 이상부터는 1 1 이렇게 나누어진다.
    A, B = map(int, input().split())
    sum = 0
    for i in range(A, B+1):
        if i >= 10:
            change_num = str(i) #바꾸고
            for c in change_num:
                sum += int(c)
        else :
            sum += i
    print(f'#{tc} {sum}')