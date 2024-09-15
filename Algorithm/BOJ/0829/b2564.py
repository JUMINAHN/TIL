import sys
#> 11:50 ~ 12 : 24(30분), 12:58~
#idx 1차원으로 잘라서 접근해보자
sys.stdin = open('input2564.txt')
C, R = map(int, input().split()) #가로, 세로의 길이
col_box = [0] * C
row_box = [0] * R
#일단 왼 <- 오 로 출발을 했을 경우 오 -> 왼이 되어야하고, 그 반대가 되어야함
s_num = int(input()) #상점의 개수 -> store_num
#상점이 1부터 구분되어야 하기 때문에
for i in range(1, s_num+1): #상점의 개수만큼 돈다.
    direct, distance = map(int, input().split()) #블록의 위치, 블록의 거리
    # idx 기준 접근을 위해서, idx위치에 append를 합니다 상점의 위치를
    if direct == 1 or direct == 2: #북쪽, row
        row_box[distance-1].append(i)
    else : #3, 4의 케이스
        col_box[distance-1].append(i)
#상점은 1이나 2나 3이라는 값이 있다
#동근이(경비원의 위치)를 구해서 넣는다.
direct, distance = map(int, input().split()) #상점의 개수를 모르니까 동근이를 무엇으로 표기할지..

#번호를 찾는다.
for i in range(1, s_num+1) : #상점의 개수만큼 돈다.
    #row나 col box에 있다면
    for j in range(1, C):
        if row_box[j] == i: #row에 있다면 #일단 왼쪽부터 -> 찾으면 어쩌구..
            pass
        if col_box[j] == i: #col에 있다면
            pass







    # 가로의 길이만큼 block 1개 생성 : 오
    # r_col_box = [0] * C
    # #세로의 길이만큼 block 1개 생성 :아
    # b_row_box = [0] * R
    # #세로의 길이만큼 block 1개 생성 : 왼
    # t_row_box = [0] * R
    # #가로의 길이만큼 block 1개 생성 : 위
    # l_col_box = [0] * C`
    # 상점이 있는 곳은 상점의 숫자로 표기하자
    # 1, 2, 3
    # 북 / 남을 나누는 거면,, 위 아래가 필요한가?
