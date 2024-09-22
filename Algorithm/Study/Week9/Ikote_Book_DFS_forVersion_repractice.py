def DFS(startV, endV):
    stack = []
    visited = [False] * (endV+1)
    result = [] #결과 값을 담을 곳

    now = startV
    stack.append(now) #현재 값
    visited[now] = True
    result.append(now) #현재 값 방문

    while stack: #stack에 값이 있다면
        now = stack[-1] #마지막 노드 -> 마지막에 남아있는 영역을 기반으로 다시 돌아간다.
        for next in graph[now]: #now 중에서
            if not visited[next] : #방문하지 않았따면?
                stack.append(next) #stack에 넣고
                visited[next] = True #방문 처리하고
                result.append(next) #6이 append되었다면
                break
        else: #인접노드가 없기 떄문에 이곳으로 들어가고
            stack.pop() #인접노드가 없을경우에 pop을 한다.

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