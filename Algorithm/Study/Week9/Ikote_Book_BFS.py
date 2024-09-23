from collections import deque

def BFS(startV, endV): #startV
    visited = [False] * (endV+1)
    queue = deque() #queue 선언
    result = []
    now = startV #현재 정점 노드
    #스택과 동일하게 큐에 담고, 방문한다.
    queue.append(now)
    visited[now] = True
    result.append(now)

    #queue가 있을떄까지 작동한다 == stack과 흐름은 동일하게 가져간다.
    while queue: #순서대로 순회할 것
        for next in graph[now]: #graph 다음 -> 다음으로
            #이전 queue에 들어있는 것은 pop해주고 이와 관련된 방문하지 않은 것들
            queue.pop()
            #방문하지 않았다면 모두 queue에 넣고, 방문처리를 한다.
            visited[next] = True
            #그리고 next와 관련된 인접노드들 queue에 넣는다.
            result.append(next)
            now = next



#각 노드가 연결된 정보
graph = [ #adj_list
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
startV = 1
endV = 8
result = BFS(startV, endV)
print(result)