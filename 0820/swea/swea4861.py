import sys

sys.stdin = open('input4861.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N*N, 찾는 것의 길이M
    arr = [list(input()) for _ in range(N)]
    #print(arr)
    
    #행 검사할 때
    print(f'#{tc}', end=" ")
    # for a in arr :
    #     if a == a[::-1]:
    #         print("".join(map(str, a)))
    #
    # #열 검사할 때
    # for col in range(N):
    #     col_data = []
    #     for row in range(N):
    #         col_data.append(arr[row][col])
    #     #열 검사
    #     reverse_col = col_data[::-1]
    #     if col_data == reverse_col:
    #         print("".join(map(str, col_data)))

    #돌아가면서 내가 원하는 숫자만큼 검사하는 방법
    #행 검사할 때
    #N만큼 순회하는 것은 맞지만,, 원래는 M까지에서 N부터 점진적으로 다가가는 것..
    for i in range(N-M+1): #0부터 20까지 배열이 있따면 -> 0부터 7까지 왜냐면 7+13이 마지막이니가 --> N-M맞지만 0이되니까 +1해줌 그러면 0만 들어감
        for row in range(i, M+i):
            row_data = []
            for col in range(i, M+i):
                row_data.append(arr[row][col])
            #열 검사
            reverse_col = row_data[::-1]
            if row_data == reverse_col:
                print("".join(map(str, row_data)))

        #열 검사할 때
        for col in range(i, M+i):
            col_data = []
            for row in range(i, M+i): #오타 유의
                col_data.append(arr[row][col])
            #열 검사
            reverse_col = col_data[::-1]
            if col_data == reverse_col:
                print("".join(map(str, col_data)))