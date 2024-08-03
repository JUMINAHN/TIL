#1. count가 증가하다가 증가하지 않을 대 total과 비교하여 클경우 지금까지의 카운트를 등록
#2. 등록하고 count reset
#3. count가 증가할 경우 계속 count화
import sys

sys.stdin = open('input9386.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #arr의 lenth
    data = list(map(int, input()))
    count = 0 # -> 1의 count만 담을 것

    total = 0
    for d in data:
        if d == 1 :
            count += 1 #코드를 보니까 마지막으로 증가하고 total과 비교를 하지 않음
        else:
            count = 0
        if total < count: #조금 비효율적이긴 하지만, 증가할떄마다 값을 넣어준다.
            total = count
    print(f'#{tc} {total}')




