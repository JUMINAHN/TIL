#count 정렬 사용
import sys

sys.stdin = open('input1204.txt')

T = int(input())
for tc in range(1, T+1):
    num = int(input()) #몇번쨰 인덱스인지?

    data = list(map(int, input().split()))
    count = [0] * 101

    for d in data:
        count[d] += 1

    max_idx = 0
    for i in range(len(count)):
        if count[max_idx] <= count[i] : #같거나 크면 -> 즉 똑같은 경우가 발생할 수 있지 않을까?
            #조건에 있음 -> 단 최빈수가 여러개일떄는 가장 큰 점수를 출력해라.
            max_idx = i
    print(f'#{num} {max_idx}')


