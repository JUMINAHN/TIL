import sys

sys.stdin = open('input4836.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #색종이 개수
    arr = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for row in range(r1, r2+1):
            for col in range(c1, c2+1): #오타 유의
                arr[row][col] += color
    #print(arr)

    total = 0
    for row in range(10): #색종이 개수만큼 돌아야 함 -> 오타 주의
        for col in range(10):
            if arr[row][col] == 3:
                total += 1
    print(f'#{tc} {total}')