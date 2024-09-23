def DFS(startV, endV): #시작노드, 끝노드
    stack = []
    visited = [False] * (endV+1) #방문 표시를 위해서
    result = [] #방문 좌표 확인을 위해서
    now = startV #현재 노드 표시를 위해서
    stack.append(now) #stack에 들어간다.
    visited[now] = True #방문을 표시한다.
    result.append(now) #경로 출력을 위해 input했다.

    #깊이 우선의 로직을 보면 작은 인접 노드의 깊이까지 파고드는 특성이 있다
    #따라서 스택에 들어가고, 방문을 표시하는 형태이다.
    while stack: #stack에 값이 있을 동안 진행된다.
        now = stack[-1] #now는 스택의 마지막 값이 고정된다.
        #이는 인접노드가 없을 떄 pop이되고 그 다음을 기반으로 인접 노드를 탐색하기 위함이다.
        for next in graph[now]:
            if not visited[next] : #다음 노드가 방문하지 않았다면
                stack.append(next)
                visited[next] = True
                result.append(next) #다음 출력을 위해서
        else : #만약 인접 노드가 없다면
            stack.pop() #마지막으로 들어간 값은 pop을 해서 사용하지 않게 한다.

    return result

#그래프의 인접 노드들
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
startV = 1
endV = 8
result = DFS(startV, endV) #시작노드, 끝노드
print(result)