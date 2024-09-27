from collections import deque

def BFS(startV, endV): #시작, 끝노드
    visited = [False] * (endV+1)
    queue = deque()
    result = []
    now = startV

    queue.append(now) #que에 담고
    visited[now] = True #방문하고
    result.append(now) #결과값에 담아서

    #queue가 끝날 떄 까지 진행
    while queue:
        now = queue.popleft() #지금 들어있는 것 기준으로 loop를 돌 것 -> 순서대로 -> 따라서 현재가 now
        for next in graph[now]:
            if not visited[next]: #방문하지 않았다면
                #관련된 것 모두 visited하고 queue에 넣는다
                queue.append(next)
                visited[next] = True
                result.append(next) #방문 순서랑 똑같으니까

    return result
#각 노드 연결된 정보
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