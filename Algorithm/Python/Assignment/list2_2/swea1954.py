#달팽이 문제
import sys

sys.stdin = open('input1954.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #배열의 범위
    snail = [[0]*N for _ in range(N)] #달팽이 초기값 설정 모두 0으로 설정할 것

    #출발 row / col 설정
    #direct 방향 설정
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]
    row = col = direct = 0
    idx = 1 #숫자를 채워넣을 것
    while idx <= N*N: #9까지 출력할 것이기 떄문에
        snail[row][col] = idx
        #마지막으로 값을 채워넣고 끝내기
        if idx == N*N:
            break
        #순서대로 채워넣기 위해서 순회
        move_row = row + data_row[direct]
        move_col = col + data_col[direct]
        if 0<=move_row<N and 0<=move_col<N and snail[move_row][move_col] == 0: #0인 곳에만 접근하기 위해서
            row = move_row
            col = move_col
            idx += 1 #idx 증가시키기
        else : #방향전환
            direct = (direct + 1) % 4
    #print(snail)
    print(f'#{tc}')
    for s in snail:
        print(*s)