# 미로탐색은 dfs보다는 bfs 푸는게 좋다 == 최단 거리
# 이 코드는 출구값이 정해져있음
# 0,0에서 시작해서 row,col에서 멈추기

from collections import deque
'''
4 6
101111
101010
101011
111011
'''

#방문표시 visited
def bfs(miro, N, M):
    queue = deque() #queue에 들어갈 친구, 시작 노드
    queue.append((0,0)) #시작 좌표

    #queue에 아무런 값이 없을 때까지
    while queue: #queue에 값이없을 떄 까지
        row, col = queue.popleft() #그러면 현재 있는 row,col의 값이 나올 것 -> 근데 단순히 해당 값이 아니라 이동되는 값에 대해서 작성을 해야할 것인데,,
        #인접 노드를 기준으로 주변 인접 노드 탐색
        # for i in miro[row][col] : #0,0일경우 -> 1,1 & 0,1인 것을 확인함 --> 즉 인접 노드 탐색을 상하좌우로 진행해야 함
        # 따라서 현좌표 기준으로 사방을 탐색해야 함
        for k in range(len(data_row)): #상하좌우 -> 이동 좌표
            move_row = row + data_row[k]
            move_col = col + data_col[k] #이동하는 것을 기준으로
            # print(move_row)
            # print(move_col)

            #이것들의 움직임 --> 이동하는 것들의 범위가 범위내에 있는지
            if not (0<=move_row<N and 0<=move_col<M) or miro[move_row][move_col] == 0: #not이 왼쪽에만 적용되는 것인지 일단 1차 궁금함
                continue #무시해 -> 진행하지 않을 것

            #만약 그게 아니라면 이제 진행할 것 -> 인접 노드로의 이동 == 그 노드로 이동
            #실제로 이동하는게 아니라 값을 기록할 것 즉 현재, 전의 +1씩해줄 것
            #즉 방문하지 않았따면 -- > 여전히 1이라면
            if miro[move_row][move_col] == 1:
                #값을 하나 증가시키고 -> 방문처리를 해주고
                miro[move_row][move_col] = miro[row][col] + 1  # 이전 노드의 1만큼씩 증가 -> 한번하고 만 느낌 ..
                #방문 처리해준 값을 다시 append로 집어넣자
                queue.append((move_row, move_col))

            #지금은 단순히 그냥 1번이고 마는 경우 -> 방문했음을 기록해야하는데 그 어떠한 값도 append를 해주고 있지 않음
            #즉 따라서 pop할게 없지 않은가?
            #어디서 무한루프?
            #현재 위치 좌표
            # print(move_row, move_col) #print안에도 못들어온다..?
            # print(miro[move_row][move_col])

    #돌려준다 언제? 무엇을? -> 마지막 값을
    return miro[N-1][M-1] #전체-1씩 더 작은 값

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)] #miro -> N과 M
#미로가 가득차있음 -> 해당 내용 탐색

#방향 전환을 위한 좌표 작성
data_row = [0, 1, 0, -1]
data_col = [1, 0, -1, 0] #우 , 하, 좌, 상

#먼저 0,0부터 탐색할 것..
#start좌표를 따로 구할 필요가 없음 -> 일단 visited 배열 없이..
#시작좌표와 끝좌표..
#최소 이동 -> 인접칸에만 접근이 가능하다.
#인접노드 접근 가능
print(bfs(miro, N, M))#일단 miro를 보낸다.
# print(miro)