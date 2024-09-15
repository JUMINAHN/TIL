import sys

sys.stdin = open('input1220.txt')
#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for col in range(N):
        prev = 0
        for row in range(N):
            n = arr[row][col]
            if n:
                if n == 2 and prev == 1:
                    ans+=1
                prev = n
    print(ans)