#DFS 재귀로 푼다면
def DFS(graph, V, visited):
    #방문을 하자
    visited[V] = True #방문을 했고
    # 방문 했음을 알립니다.
    print(V, end=" ") #방문하자말자 -> 방문했음을 알립니다
    #graph의 인접노드들을 탐색하자
    for i in graph[V]: #1부터 인접노드를 스택구조로 탐색한다
        #돌아서 재귀 구조로 탐색하기
        #만약 방문하지 않았다면 방문을 시킬 것
        if not visited[i]:
            DFS(graph, i, visited)

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
#그래프 시작 1번, 총 8개
Node_count = 8
startV = 1
visited = [False] * (Node_count+1) #총 9개
DFS(graph, startV, visited)