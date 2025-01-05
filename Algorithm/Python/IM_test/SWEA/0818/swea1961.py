import sys

sys.stdin = open('input1961.txt')


def turn(arr, N):
    new_arr = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            new_arr[row][col] = arr[N - 1 - col][row]
    return new_arr

#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #N*N 행렬이 주어질때 90도 180도 270도 회전한 모양 출력
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    #90도 회전, 원본 기준 새로운 배열 생성
    arr90 = turn(arr,N)
    arr180 = turn(arr90, N)
    arr270 = turn(arr180, N)
    arrzip = list(zip(arr90, arr180, arr270))

    print(f'#{tc}')
    for a, b, c in arrzip:
        print("".join(map(str, a)), "".join(map(str, b)), "".join(map(str, c)))
