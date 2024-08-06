import sys

sys.stdin = open('input1215.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]

    #전체를 돌면서 범위를 탐색 -> 원하는 길이
    #회문의 특징을 기억하자
    #헷갈리면 row / col을 구분하자
    #배열에서 원하는 길이르 추출하려면 out of range가 뜰 수 있기 떄문에 start값 설정에 유의하자

    #행기준 -> 열 우선 계산
    count = 0
    for row in range(8):
        for col in range(8-N+1):

            for k in range(N // 2) : #가운데 값을 찾아서
                if arr[row][col + k] != arr[row][col + N-1-k]:
                    break
            else:
                count += 1

    for col in range(8):
        for row in range(8 - N + 1):

            for k in range(N // 2):  # 가운데 값을 찾아서
                if arr[row + k][col] != arr[row + N - 1 - k][col]:
                    break
            else:
                count += 1
    print(f'#{tc} {count}')

