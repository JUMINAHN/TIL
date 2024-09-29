'''
5 6
101010
111111
000001
111111
111111
'''
from collections import deque
def BFS(row, col):# rowcol의 좌표 위치
    #일단 queue를 선언하고, 방문에 대한 것을 진행할 것
    queue = deque() #받았고
    queue.append((row, col)) #현재의 row -> col을 append 받음 -> 그리고 여기서 이동하는게 아니라 다음에 영향

    #queue에 값이 없을 떄까지 탐색할 것
    while queue:
        r, c = queue.popleft() #이것을 기반으로
        for k in range(len(data_row)): #방향 전환을 돌 친구
            move_r = r + data_row[k]
            move_c = c + data_col[k]
            #이게 범위를 초과하는가? 그리고 0인지 아닌지
            #초과하면 범위 벗어남 + 그리고 0이면 범위 벗어남
            if not (0<=move_r<N and 0<=move_c<M) or miro[move_r][move_c] == 0:
                continue
            if miro[move_r][move_c] == 1:
                #방문 처리
                miro[move_r][move_c] = miro[r][c] + 1 #지금 이 처음값에 대해서 == quepop으로 받은것에 대해서
                queue.append((move_r, move_c)) #인접노드들 닫 들어갈 것
    return miro[N-1][M-1]

    #그리고 방향 전환을 실시할 것

N, M = map(int, input().split())
#미로 채우기
miro = [list(map(int, input())) for _ in range(N)] #미로를 채우고
#방향 전환을 위한 방향을 설정
#우/좌/하/상
data_row = [0,0,1,-1]
data_col = [1,-1,0,0]
#그리고 이걸 기반으로 BFS가 탐색할 것 -> 첫번쨰 노드가 0,0
print(BFS(0,0))
print(miro)
#[3, 0, 5, 0, 7, 0],
#[2, 3, 4, 5, 6, 7],
#[0, 0, 0, 0, 0, 8],
#[14, 13, 12, 11, 10, 9],
# [15, 14, 13, 12, 11, 10]]