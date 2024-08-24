import sys

sys.stdin = open('input2005.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if col == row :
                arr[row][col] = 1
            if col > row :
                arr[row][col] = ''
            if col == 0 :
                arr[row][col] = 1
    #print(arr)
    for row in range(N):
        for col in range(N):
            if 0<= row < N and 0 <= col < N and arr[row][col] == 0 :
                arr[row][col] = arr[row-1][col] + arr[row-1][col-1]
    print(f'#{tc}')
    for a in arr:
        print(" ".join(map(str, a)))