import sys

sys.stdin = open('input1989.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = input()
    compare = N[::-1] #N자체를 역순으로 하는 것
    #print(compare)
    if N == compare:
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')