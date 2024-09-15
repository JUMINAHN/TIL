import sys

sys.stdin = open('input4864.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    i = 0
    for s2 in str2:
        if len(str1) == i:
            break
        if s2 == str1[0+i]:
            i += 1 # i를 증가시키고
        else :
            i = 0

    if len(str1) == i:
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')