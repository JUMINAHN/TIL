#정방향 쉬운 문제
import sys

sys.stdin = open('input19606.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total_cross1 = total_cross2 = 0
    for row in range(N):
        total_cross1 += arr[row][row]
        total_cross2 += arr[row][N-1-row]
    #가장 가운데 자리 빼줘야 함
    print(f'#{tc} {total_cross1 + total_cross2 - arr[N//2][N//2]}')
