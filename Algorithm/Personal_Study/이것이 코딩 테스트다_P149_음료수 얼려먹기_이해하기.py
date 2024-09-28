#2024-09-27
'''
4 5
00110
00011
11111
00000
'''
#델타는 bfs나 반복에 많이 사용
#DFS로 특정 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def DFS(x, y): #x좌표 y좌표 리스트 하나 하나씩
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M: #0보다 작으면 안되고 N보다 크거나 같으면 안됨
        #if not (0 <= x < N and 0 <= y < M): 이렇게도 사용할 수 있음
        return False # 해당 범위를 벗어나면 안되기 때문에
    #현재 노드를 방문하지 않았따면?
    if graph[x][y] == 0: #0이 미방문 지역 -> row, col에 방문하지 않았다면
        graph[x][y] = 1 #방문 처리하기 -> true/false 대신
        DFS(x-1,y) #해당 범위?? : 상
        DFS(x,y-1) #좌
        DFS(x+1,y) #하
        DFS(x,y+1) #우
        return True #방문했따면 방문 성공한것이고
    return False    # 아니면 실패 그자체인 것


#코드 이해하기
N, M = map(int, input().split())

#2차원 리스트의 맵 정보 입력받기
graph = [] #인접노드
for i in range(N): #행
    graph.append(list(map(int ,input()))) #graph에 추가한다. 한줄씩 -> list형태로
#input받아서 채워넣기

result = 0 #모든 노드에 대해 음료수 채우기
for i in range(N):
    for j in range(M):
        #현재 위치에서 DFS 수행
        if DFS(i,j) == True:
            result += 1
#각 영역을 하나의 아이스크림으로 간주
#모든 칸을 순회
# 각 칸에서 DFS를 시작하여 새로운 아이스크림 영역을 찾습니다
#그래프의 각 칸(i, j)에 대해 DFS를 호출 -> 이미 방문했으면 false를 반환하고 다음칸
#방문하지 않은 칸이면 그 칸에서 dfs시작 -> 이 칸을 중심으로 연결된 것들 찾아냄

print(result)


'''
#생각한 것
#0으로 연결된 인접노드들 탐색하고 공간확인
#0의 노드를 벗어나면 끝 -> 그 전까지를 한가지의 덩어리로 인식
#또 다른 0을 찾으면 하나의 덩어리로 생성됨
#총 묶음 덩어리 결과값 도출 
'''