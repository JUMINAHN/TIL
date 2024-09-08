import sys

sys.stdin = open('input20379.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]

    #행 -> 열 모두 탐색
    max_len = 0
    for row in range(N):
        count_len = 0
        for col in range(M):
            if ground[row][col] == 1 :
                count_len += 1
            else :
                if max_len < count_len and count_len > 1:
                    max_len = count_len
                count_len = 0 #아니면 초기화
        if max_len < count_len and count_len > 1:
            max_len = count_len
    ground2 = list(map(list, zip(*ground))) #전치 행렬
    for row in range(M):
        count_len = 0
        for col in range(N):
            if ground2[row][col] == 1:
                count_len += 1
            else :
                if max_len < count_len and count_len > 1: #1보다 커야함
                    max_len = count_len
                count_len = 0 #아니면 초기화
        if max_len < count_len and count_len > 1:
            max_len = count_len
    #조건문 오타
    print(f'#{tc} {max_len}')