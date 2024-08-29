import sys

sys.stdin = open('input2805.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #농장의 크기
    #농작물의 가치
    value = [list(map(int, input())) for _ in range(N)] #농작물 가치들 나열해서
    #이 농작물들을 달팽이처럼 돌 것임

    #이동방향 설정
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]
    #초기값 setting
    row = col = direct = 0
    #모두 회전이 끝날때를 무엇으로 설정..?
    #모두 pop을 해서 배열에 남기지 않는다면..?
    #순회 -> 내부에 모두 6이 없을때 까지..

    #조건 i
    i = 0
    finish_total = 0
    #먼저 달팽이처럼 돌자
    while finish_total != (N*N*6): #value가 없으면 자동으로 없어지겠지
        #if row == i and row == (N-1-i): #이거 일 때, 그리고 범위가 어느정도 정해져있을 것 --> keep
        move_row = row + data_row[direct]
        move_col = col + data_col[direct]
        if 0 <= move_row < N and 0 <= move_col < N and value[move_row][move_col] != 6: #이동하고
            #현재 있는 값을 pop해준다. -> pop은 idx를 해주는 것.. 흠 어떻게 접근하면 좋을지 모르겠다.
            value[row][col] = 6 #지나온 값은 6으로 채워준다.
            row = move_row
            col = move_col
        else :
            direct = (direct + 1) % 4 #아니면 방향을 전환하고
