def DFS(startV, endV):
    stack = []
    visited = [False] * (endV+1)
    result = []

    now = startV
    visited[now] = True
    result.append(now)
    stack.append(now)
    while stack:
        now = stack[-1]  # 스택의 top을 현재 노드로 설정
        #스택의 top은 항상 현재 탐색 중인 노드
        #새로운 노드를 방문할때마다 현재 위치 갱신
        #스택의 top이 항상 현재 탐색 중인 노드와 일치하도록 보장
        #더 이상 방문할 인접 노드가 없을 떄 자동으로 이전 노드로 돌아갈 수 있도록 한다.
        for next in graph[now]:
            if not visited[next]:
                stack.append(next)  # 다음 노드를 스택에 추가
                visited[next] = True
                result.append(next)
                break
        else: #break를 만나지 않을 경우 실행
            stack.pop()  # 더 이상 방문할 인접 노드가 없으면 pop
            #6에서 pop당함

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
result = DFS(startV, endV)
print(result)

