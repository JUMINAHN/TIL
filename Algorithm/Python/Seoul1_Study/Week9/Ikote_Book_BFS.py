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
        now = queue.popleft() #방문을 하고
        for next in graph[now]: #pop한 내용을 기반으로 graph 탐색
            if not visited[next]:
                #방문하지 않았다면 모두 queue에 넣고, 방문처리를 한다.
                queue.append(next)
                visited[next] = True
                #그리고 next와 관련된 인접노드들 queue에 넣는다.
                result.append(next) #근데 이러면 그게 되나?
                #3번째 idx가 예를 들면 1, 4, 5가 들어갔다면  그냥 그 숫자는 없어지는 것
    return result #구조를 생각하자

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