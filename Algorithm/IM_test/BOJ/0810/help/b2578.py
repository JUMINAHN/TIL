import sys
sys.stdin = open('input2578.txt')

bingopan = [list(map(int, input().split())) for _ in range(5)]
talk_num = [list(map(int, input().split())) for _ in range(5)]
talk = []
for t in talk_num:
    talk.extend(t)
#print(talk)
#빙고판의 색칠은 랜덤 누적을 구해야한다 -> count 정렬의 방식으로 접근하는 것이 좋으며, 이를 위해 idx로 좌표를 생성한다.
position = [0] * 26
for row in range(5):
    for col in range(5):
        position[bingopan[row][col]] = (row, col) #좌표를 각각 심어준다.

#본격적인 계산을 진행한다. 이를 위해서 각 행/열/대각1/대각2에 누적할 수 있는 데이터 표를 만들어야한다.
#대각선은 수가 9개까지 들어간다.
visited = [[0]*10 for _ in range(4)]
#사회자가 말하는 내용을 기반으로 위치를 찾는다
for idx, t in enumerate(talk):
    row, col = position[t] #열/행/대1/대2순으로 가자
    visited[0][col] +=1
    visited[1][row] +=1
    visited[2][row-col] +=1
    visited[3][row+col] +=1

    # visitied한 곳에 1이상인지 확인한다.
    count = 0
    for v in visited:
        #값이 5개인 요소를 리스트 안에서 세는 것
        for value in v:
            if value == 5:
                count += 1
    if count >= 3:  # 몇번째 수
        print(idx+1)
        break