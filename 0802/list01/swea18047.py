import sys

sys.stdin = open('input18047.txt')

T = int(input()) #testcase 3
for tc in range(1, T+1):
    N,M = map(int, input().split()) #10, 3
    ai = list(map(int, input().split())) #1 2 3 4 ....9 10

    #기준점으로 둘 값
    new_arr = ai[0:M]
    new_total = 0
    for new_a in new_arr:
        new_total += new_a
    min_total = new_total #0으로 두면 0이 제일 작은값이 나오기 때문에 해당 되지 않을 것임
    max_total = 0
    for i in range(N) : #1부터 10까지 --> 0부터 9까지 ai의 길이
        sum = 0
        if i == N-M+1:
            break
        for j in range(i, i+M) : #0부터 M-1번까지 index를 찾아서 순회
            sum += ai[j]
        if max_total < sum:
            max_total = sum
        if min_total > sum:
            min_total = sum
    print(f'#{tc} {max_total - min_total}')
