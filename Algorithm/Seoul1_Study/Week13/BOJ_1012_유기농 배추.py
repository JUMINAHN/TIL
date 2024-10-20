#주석이 없는 것
def dfs(field, row, col):
    field[row][col] = 0
    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]
    for i in range(len(data_row)):
        move_row = row + data_row[i]
        move_col = col + data_col[i]

        if not(0<=move_row<N and 0<=move_col<M) or field[move_row][move_col] == 0:
            continue
        if field[move_row][move_col] == 1:
            field[move_row][move_col] = 0
            dfs(field, move_row, move_col)
    return
T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    pos = [list(map(int, input().split())) for _ in range(K)]

    for p in pos:
        x = p[1]
        y = p[0]
        field[x][y] = 1
    count = 0
    for row in range(N):
        for col in range(M):
            if field[row][col] == 1:
                count += 1
                dfs(field, row, col)
    print(count)
'------------------------'
#주석이 있는 것
#이코테에서 봤던 얼음틀 문제와 유사
#오잉..?? 출력은 한번만에 했따 이게 왜 돼? 알수없다..
#RECURSIONeRROR 발생
import sys
sys.setrecursionlimit(10**6) #이건 나중에 기억해둬야할듯?
input = sys.stdin.readline
#해당 문제는 for문으로 arr[row][col]에 접근해서 해당 값이 1이면 count += 1을 해주는 문제
#그리고 이렇게 count 1을 해준 곳은 모두 0으로 만들어서 방문 했흠을 표시한다.
#해당 문제에서 특이한 점은 input값인데 arr로 만들어서 기존 배열에 값을 담아주면 될 것 같다

def dfs(field, row, col):
    #자 일단 현재 위치를 방문 처리한다.
    field[row][col] = 0 #나 방문했어요
    #그리고 해당 부분은 특정 좌표를 벗어나면 안된다. == 얘는 네방형으로
    #따라서 방향 이동이 필요함

    data_row = [0, 1, 0, -1]
    data_col = [1, 0, -1, 0]
    #방향 전환 준비 == 나를 기점으로
    for i in range(len(data_row)): #4방향으로
        move_row = row + data_row[i]
        move_col = col + data_col[i]

        if not(0<=move_row<N and 0<=move_col<M) or field[move_row][move_col] == 0: #0이면
            continue #방문할 필요가 없다

        if field[move_row][move_col] == 1: #1번이면 -> 방문해야한다.
            field[move_row][move_col] = 0
            #방문을 처리하고, 또 그 인접노드로 이동을 해야한다.
            #따라서 여기서 재귀
            dfs(field, move_row, move_col) #또 방문 여부를 확인한다.
    return #딱히 리턴으로 돌려줄 것은 없음

#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split()) #가로, 세로(row), 지렁이가 있는 pos
    #배추밭을 만들 것
    field = [[0]*M for _ in range(N)] #배추밭만큼 0을 채운다
    #우리는 지렁이가 있는 좌표를 받을 것
    pos = [list(map(int, input().split())) for _ in range(K)] #list값으로 좌표를 받을 것
    #자 이제 지렁이가 있는 곳을 배추밭에 표기한다.
#    print(pos)
#     for p in pos:
#         print(p[0], p[1]) #좌표가 거꾸로 되어있는 것을 간과함
    for p in pos:
        x = p[1] #실수 방지를 위해서 명확하게 변수를 표기한다.
        y = p[0]
        field[x][y] = 1 #field의 받은 좌표 지점에 지렁이가 있음을 나타낸다 == 1은 지렁이가 있음을 나타내는 것
    #
    # #자 이제 지렁이가 있는 것 까지 표기를 완료했다. 우리는 이제 최소의 배추 지렁이 마리수를 뽑아야 한다.
    count = 0 #지렁이가 있는 것을 계산하기 위한 변수명
    for row in range(N):
        for col in range(M):
            if field[row][col] == 1: #해당 좌표가 1이면
                #우리는 count할 것입니다.
                count += 1
                #단, 인접 노드를 모두 탐색할 것입니다. -->  인접노드 방문 처리를 진행해야 한다.
                dfs(field, row, col)#현재 row,col이 필요하지 않을까? 왜냐하면 인접 노드를 탐색해야 하기 떄문에
    print(count) #그래서 그게 몇번 카운팅 되었는지 확인한다.