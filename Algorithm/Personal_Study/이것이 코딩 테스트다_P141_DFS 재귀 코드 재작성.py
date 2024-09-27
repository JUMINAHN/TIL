def DFS(graph, V, visited) : #정점
    #V노드 방문
    visited[V] = True
    print(V, end=" ") #방문을 했음을 나타내기

    for i in graph[V]: #재귀로 탐색
        #방문하지 않은 곳들에 대해서 -> 구조적으로 생각
        if not visited[i]:
            DFS(graph, i, visited) #잘못찍음

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
#그래프
visited = [False] * 9
startV = 1
DFS(graph, startV, visited)