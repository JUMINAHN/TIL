#모든 지점까지의 거리를 구하기
#n은 세로, m은 가로
#0은 갈 수 없는 땅, 1은 갈 수 있는 땅, 2는 목표지점
#목표지점까지의 거리 -> 2부터 시작하고, 맨 마지막 좌표가 마지막
#현재 좌표에서는 0,0이 2인데 아닐 수도 있다는 것 == 즉 2의 좌표 위치를 찾아야 함
#도달할 수 없는 땅은 막혀있는 땅은 -1로 바꿀 것 ==???
'''
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
'''

# N*M
# startnode == find
# 똑같이 0에는 접근할 수 없음을 기록하면 끝인 문제 == 미로 탈출과 동일하나 2의 좌표 위치가 바뀜
# 2가 0,0일수도 5,5일수도 N-1,M-1일수도?? == 그럼 끝노드는 어떻게 찾는가? (상관이 없는가?) 일단 작성해보자

from collections import deque #queue -> 방문 표시, queue에 넣어줘야 함
def bfs(ground, start_row, start_col): #일단은 땅 자체를 받음, 시작 좌표와 끝 좌표를
    # if ground[start_row][start_col] == 2: #2인게 확정이 되어있지만 -> 담고 초기화해서 그런줄 알았는데 또 그것은 아님
    #     ground[start_row][start_col] = 0
    queue = deque() #queue에 담아서 pop을 해야하기 떄문에
    queue.append((start_row, start_col)) #해당 값을 전달받음 -> 갈수있는길이 아니게 되더라도 상관없지 않나

    #그리고 일단은 -> 해당 좌표도 방문 처리를 진행해줘야 하는데
    #bfs는 dfs와 다르게 처음값만 받고 그 뒤에부터 밑에서 활용하기 떄문에 괜찮음

    while queue:
        row, col = queue.popleft() #해당 값을 활용할 것
        #범위를 벗어나는 것 확인하기 전에 일단 2인 좌표부터 방문 처리를 진행해준다.
        # if ground[row][col] == 2: -> 2가 모두 0으로 됨
            #ground[row][col] = 0 # 0으로 방문 처리해주고
        #자 그리고 -> 인접 노드들을 탐색할 것인데 -> 이는 상하좌우로 밖에 이동을 못한다는 규칙이 있음 -> 따라서 4방향으로 가는 위치를 탐색한다.
        for k in range(len(data_row)):
            move_row = row + data_row[k]
            move_col = col + data_col[k] #상하좌우로 가고

            #해당 값이 범위를 벗어나는지 먼저 확인 -> not은 괄호에만 적용이 됨
            #if (not (0<=move_row<N and 0<=move_col<M)) or (ground[row][col] == 0): => 두개 다 적용하려면 or뒤에 not해야함
            # if not (0<=move_row<N and 0<=move_col<M) or ground[move_row][move_col] == 0: #현재가 아님 -> 이거 확인..!! 오탈자 제발ㅈ ㅏㄹ보기
            #     continue #볼필요도 없으니까

            # if ground[start_row][start_col] != 0: #>> 0이라는 것인데 왜? 우 하가 3이 나오는가?
            #    ground[move_row][move_col] = ground[start_row][start_col] + 1

            if (0<=move_row<N and 0<=move_col<M) and ground[move_row][move_col] == -1: #1이라면 -> 갈 수 있는 것
                #방문 처리를 한다 => 무엇으로? 이전값 +1로 -> 방문 처리를 한다.
                # if flag == True:
                #     flag = False
                #     continue #
                #스타트 노드랑 인접노드일떄는 패스하기 --> how?  :: 또 for문으로 돌리는 것을 생각했는데 너무 복잡해짐
                ground[move_row][move_col] = ground[row][col] + 1#queue에서 pop한 것이 무엇인지 생각하면 됨 => 그니까 실제 거리까지 해줘 함
                #이떄까지 현재 위치의 값에 1을 넣는 방식을 사용했었음
                #그리고 queue에 다시 이동하는 곳에 대한 값을 넣어준다.
                queue.append((move_row, move_col)) #append가 제대로 되지 않는듯 하다..? -> 그 다음값으로 하면 되는데..? -> 주는 것도 증가시켜야 함
        #print(ground, 'check')
    # count += 1
    return ground

#행, 열
N, M = list(map(int, input().split())) #15, 15 정사각형
ground = [list(map(int,input().split())) for _ in range(N)] #input받아서 들어와진다.

#일단 좌표를 움직일 것이니까 -> 이동 범위 설정
#우하좌상
data_row = [0,1,0,-1]
data_col = [1,0,-1,0]

#input 내용 -> visited할 필요 없이 그냥 진행


#그 전에 2가 있는 곳의 좌표를 알아야 그 뒤 작업을 진행할 수 있을 것 같다
start_row = start_col = 0
flag = True
for row in range(N):
    for col in range(M):
        if ground[row][col] == 2:
            start_row = row
            start_col = col
            flag = False
            break
    if flag == False: #False라면? -> 이거 잘 보기
        break

#print(start_row, start_col)
#방문 처리를 해볼까?-> 근데 쓸필요가 없는데
#print(ground)
#ground 자체를 다시 넘겨받는다면, 출력에 문제가 없을듯
#아닌 것도 찾아야 하니 -> 1을 -1로 바꿔주고, 시작 노드 좌표도 0으로
#이 부분이 key point였음 --> gpt도움받음
for row in range(N):
    for col in range(M):
        if ground[row][col] == 2: 
            ground[row][col] = 0
        elif ground[row][col] == 1:
            ground[row][col] = -1 #-1인것만 탐색하면 됨

result = bfs(ground, start_row, start_col)

for r in result:
    print(*r)