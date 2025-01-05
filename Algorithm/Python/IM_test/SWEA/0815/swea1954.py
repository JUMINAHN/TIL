import sys

sys.stdin = open('input1954.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #1. 달팽이는 N*N 시계방향 : 오른쪽부터 아래, 왼쪽, 위
    #2. 정수N을 입력받아서 N크기의 달팽이 출력 -> 백준의 자리배정
    N = int(input())
    #N*N크기의 배열 생성
    arr = [[0] * N for _ in range(N)]
    #이 배열에 하나씩 채워주기

    #이동하면서 접근하고, 채워주는 것을 진행해야되기 때문에 for문보다는 while을 사용하자
    #칸을 채우면서 이동하는 것은 델타를 사용하면 좋다.
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]
    idx = 1 #1부터 시작! #초기값 설정
    row = col = direction = 0 #0,0 idx부터 시작하니까
    while idx <= N*N: #일떄 까지
        arr[row][col] = idx #idx는 계속해서 증가해야 한다.
        if idx == N*N:
            break
        #그리고 이것을 기점으로 한쪽방향으로 갔다가 범위가 초과되면 방향을 트는것으로 한다.
        move_row = row + data_row[direction]
        move_col = col + data_col[direction]

        ##지금 보면 0이 아닌 것을 덮어 씌우는 문제가 있다
        #따라서 이동할 곳이 0일 경우에만 값을 추가하고 넣는다
        if 0 <= move_row < N and 0 <= move_col < N and arr[move_row][move_col] == 0:
            #이동하는 move를 현재나의 row에 대입한다.
            row = move_row
            col = move_col
            idx += 1 #방향을 틀꺼니까. -> idx 순번값 증가
        else:
            #범위가 벗어나게 되면, 방향을 일단 전환해준다.
            direction = (direction + 1) % 4
    print(f'#{tc}')
    for a in arr:
        print(*a) #unpacking을 해서 리스트 값 모두 꺼내기