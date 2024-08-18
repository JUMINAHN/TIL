import sys

sys.stdin = open('input1954.txt')
#테스트 케이스 개수
T = int(input()) #2
for tc in range(1, T+1):
    N = int(input()) #N*N의 크기의 배열, 그 부분을 모두 순회할 것
    spin = [[0]*N for _ in range(N)]

    #spin을 돌면서 하나씩 접근할 것이고, 이동할 것
    #내 영역에서 범위를 확대하는 것이 아니라 나 자체를 이동하는 것 => while 사용
    idx = 1
    row = col = direction = 0 #row,col이 0인것부터 시작할 것

    #회전의 우선순위 오 하 좌 위
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]

    while idx <= N*N:
        #일단 현재 data에 값 입력
        spin[row][col] = idx
        #idx 16을 채우고 끝내기
        if idx == N*N:
            break

        move_row = row + data_row[direction]
        move_col = col + data_col[direction]
        #그리고 0인 곳에만 접근할 수 있도록 설정해야함
        if 0<=move_row<N and 0<=move_col<N and spin[move_row][move_col] == 0:
            row = move_row
            col = move_col
            idx += 1 #회전이 가능할경우 idx를 하나 증가시킨다.
        else: #저 범위가 아닐경우는 회전을 한다.
            direction = (direction + 1) %4 #4방향에 대해서
    print(f'#{tc}')
    for s in spin:
        print(*s)
