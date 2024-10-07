# 미로탐색은 dfs보다는 bfs 푸는게 좋다 == 최단 거리
# 이 코드는 출구값이 정해져있음
# 0,0에서 시작해서 row,col에서 멈추기
from collections import deque

#방문표시 visited
def bfs(miro, N, M):
    queue = deque() #queue에 들어갈 친구, 시작 노드
    queue.append((0,0)) #시작 좌표

    #queue에 아무런 값이 없을 때까지
    while queue: #queue에 값이없을 떄 까지
        row, col = queue.popleft() #그러면 현재 있는 row,col의 값이 나올 것 -> 근데 단순히 해당 값이 아니라 이동되는 값에 대해서 작성을 해야할 것인데,,
        #인접 노드
        #이것들의 움직임
        if not (0<=row<N and 0<=col<M) or miro[row][col] == 1: #1이 아닐때
            continue #무시해 -> 진행하지 않을 것
        #만약 그게 아니라면 이제 진행할 것 -> 인접 노드로의 이동동



N, M = map(int, input().split())
miro = [list(input()) for _ in range(N)] #miro -> N과 M
#미로가 가득차있음 -> 해당 내용 탐색


#먼저 0,0부터 탐색할 것..
#start좌표를 따로 구할 필요가 없음 -> 일단 visited 배열 없이..
#시작좌표와 끝좌표..
#최소 이동 -> 인접칸에만 접근이 가능하다.
#인접노드 접근 가능
bfs(miro, N, M) #일단 miro를 보낸다.