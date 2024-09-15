import sys

sys.stdin = open('input18059.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #색칠되는 것 개수
    arr = [[0] * 11 for _ in range(11)]

    total = 0
    for i in range(N): #N번 반복해서 해당 내용 반복
        r1,c1,r2,c2,rgb = map(int, input().split())

        #전체에서 해당되는 것만 색칠 -> 이동하는게 아니라 그 영역만 색칠하는 것
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                if arr[row][col] == 0:
                    arr[row][col] = rgb
                else :
                    arr[row][col] += rgb

        for row in range(11):
            for col in range(11):
                if arr[row][col] == 3:
                    total += 1

    print(f'#{tc} {total}')