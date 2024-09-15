import sys

sys.stdin = open('input4864.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')