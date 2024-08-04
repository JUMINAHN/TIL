import sys

sys.stdin = open('input1954.txt')

T = int(input())
for tc in range(1, T+1):
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]

    N = int(input()) #N*N사이즈
    arr = [[0]*N for _ in range(N)] #배열이 만들어져있다 --> 이곳에 값을 채워 넣자

    #arr에 가장 첫번째 인덱스를 세팅해주자
    #k는 이동할 횟수다
    row, col, num, k = 0, 0, 1, 0

    arr[row][col] = num #그래서 이건 1이다
    num += 1 #2부터의 값이 들어가야 하니까까
    while num <= N*N:
        move_row = row + data_row[k] #이동을 측정할 row
        move_col = col + data_col[k]

        if 0<= move_row < N and 0 <= move_col < N and arr[move_row][move_col] == 0:
            row = move_row #for로 순환이 되지 않기 떄문에 이동 지역을 자체적으로 반영시켜줌
            col = move_col
            arr[row][col] = num #전체 --> num2이 처음에 2로 들어감
            num += 1 #해당 되면 또 다른 값이 증가되어야 하기 떄문에
        else :
            k = (k+1) % 4 #k값은 계속 증가될 것이고 4라는 범위 안팍에서 이루어져야 하기 떄문에 해당 공식사용
    print(f'#{tc}')
    for a in arr:
       print(*a)

