#delta로 접근하기 좋은 풍선팡 문제
import sys

sys.stdin = open('input9490.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N * M개 풍선 /  A개의 꽃가루 개수
    arr = [list(map(int, input().split())) for _ in range(N)] #행의 개수 -> N

    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]

    total = 0
    #최대값을 출력하는 델타 -> 꽃가루 날리기
    for row in range(N):
        for col in range(M):
            A = arr[row][col]
            s = 0
            for i in range(1, A + 1):
                for k in range(len(data_row)):
                    move_row = row + data_row[k] * i #무엇을 곱할지에 대한 실수 조심
                    move_col = col + data_col[k] * i

                    if 0<=move_row<N and 0 <= move_col<M:
                        s += arr[move_row][move_col]
            s += arr[row][col]
            if total < s :
                total = s
    print(f'#{tc} {total}')