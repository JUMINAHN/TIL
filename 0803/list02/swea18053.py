#count 정렬을 사용하면 될 것 같음
import sys

sys.stdin = open('input18053.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #배열의 길이 --> data == ai

    ai = list(map(int, input()))
    count = [0] * 10 #0부터 9까지 들어갈 것임

    #1.각 숫자의 개수를 살린다.
    for a in ai:
        count[a] += 1

    #2. 합을 구한다.
    max_idx = 0 #어떤 숫자가 많은지 -> idx 기준
    max_num = 0 #count 개수
    for i in range(len(count)):
        if max_num <= count[i]: #동일하게 같은값이 있을 수 있음 -> #카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다
            max_num = count[i]
            max_idx = i
    print(f'#{tc} {max_idx} {max_num}')
