#2024-09-28
def DFS(graph, V, visited) : #V로 바꾼 이유는, 시작 노드의 값이 계속 바뀜 -> 헷갈릴까봐
    #지금 노드는 방문한 상태 -> 방문한 것 확인을 위한 출력
    visited[V] = True
    print(V, end= " ")
    #나머지 방문 여부 확인하기 DFS로 -> 그림 로직 생각해보기
    for i in graph[V]: #그래프 인접노드를 모두 DFS로 탐색할 것 -> 가장 작은 값 부터 깊이 우선으로 탐색하는 것을 알 수 있음
        #방문하지 않은 것에 대한 방문 처리를 진행해줘야 함
        if not visited[i]: #방문할 수 있도록 재귀 호출
            DFS(graph, i, visited) #i를 방문 시킬거니까

graph = [
    [], #0번 idx를 사용하지 않는 것에 대한 누락 : 해당 부분 유의
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
#시작 노드
startV = 1
#총 노드
totalNode = 8
visited = [False] * (totalNode + 1) #왜냐하면 0이 값에 없기 떄문에
DFS(graph, startV, visited)