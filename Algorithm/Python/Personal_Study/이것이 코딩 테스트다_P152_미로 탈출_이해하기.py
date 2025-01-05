'''
5 6
101010
111111
000001
111111
111111
'''
from collections import deque
#기본 bfs 구조 동일하게 진행되는 코드
#stack 형식 재귀 bfs보다는 코드가 길지만 구조는 동일함
#이동하는거 자체가 아니라 내부 값을 채울 것이니까 -> while처럼 이동하지않고 내부 값을 채울때

def BFS(x, y):
    #내부에서 queue설정
    queue = deque()
    queue.append((x,y)) #queue에 값을 넣고
    #값이 있는 것
    while queue: #queue에 값이 없을 떄 까지
        x, y = queue.popleft()
        #이 x,y가 이동해야 함
        #방향 전환을 해야 함
        for k in range(len(data_row)):
            move_row = x + data_row[k]
            move_col = y + data_col[k]
            #일단 범위가 벗어나지 않도록 해야하고 0이면 갈 수 없음 -> 0이면 아무런 행위도 하지 않고 되돌아가야함
            if not (0<=move_row<N and 0<=move_col<M ) or (miro[move_row][move_col] == 0): #1인 지역에만 갈 수 있음
                continue #다시돌아가고
            if miro[move_row][move_col] == 1: #1인 곳이라면 -> 내가 원하는 길 -> 내꺼 내용 pass
                #queue -> 방문하지 않았다는 의미니까
                #기존값 보다 1증가
                miro[move_row][move_col] = (miro[x][y] + 1) #기존 값이니까 -> 여기서 증가시키는 것
                queue.append((move_row, move_col)) #이동자체를 보낼 것임
    return miro[N-1][M-1]#최종적으로 마지막 노드의 값 반환

N, M = map(int, input().split())
#미로 채우기
miro = [list(map(int, input())) for _ in range(N)]

#이동할 방향 범위 설정
#올라가는 케이스를 마지막으로 두고  우 /좌 / 하 / 상 으로 간다.
data_row = [0, 0, 1, -1]
data_col = [1, -1, 0, 0]

print(BFS(0,0)) #시작노드에서 출발한다.