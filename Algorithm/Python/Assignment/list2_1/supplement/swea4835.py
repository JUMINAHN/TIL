import sys

sys.stdin = open('input4835.txt')

T = int(input())
for tc in range(1, T+1):
    #일단 배열의 길이는 N이고, 추출할 split or range가 M
    N, M = map(int, input().split()) #N개의 정수가들어있는 배열에서, 이웃한 M개의 합
    ai = list(map(int, input().split())) #N개의 개수

    #가장 작은 것, 가장 큰 것의 차
    #min_total = sum(ai[0:N])
    min_total = 0
    max_total = 0
    for i in range(N): #n-1까지 들어가 있음
        if i == N-M+1:
            break
        s = 0
        for j in range(i, i+M):
            s += ai[j]
        if i == 0:
            min_total = s

        if max_total < s :
            max_total = s
        if min_total > s:
            min_total = s
    print(f'{tc} {max_total-min_total}')
