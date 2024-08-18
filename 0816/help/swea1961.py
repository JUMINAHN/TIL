import sys

sys.stdin = open('input1961.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    def rotate(arr):
        arrR = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                arrR[i][j] = arr[N - 1 - j][i]
        return arrR


    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr1 = rotate(arr)
    arr2 = rotate(arr1)
    arr3 = rotate(arr2)

    print(arr1)
    print(arr2)
    print(arr3)
    #list 하나 자체가 묶여있다보니 원하는 요구조건에 따라 리스트 하나씩 출력되는 것으로 확인됨

    # print(f'#{tc}')
    # for a, b, c in zip(arr1, arr2, arr3):
    #     print(f'{"".join(map(str, a))} {"".join(map(str, b))} {"".join(map(str, c))}')