#왜 오류? 1,2,7,6에서 멈춤
def DFS(startV, endV):
    stack = []
    visited = [False] * (endV+1) #방문 정점의 개수를 확인하기 위해
    result = [] #방문 순서를 기록하기 위해

    now = startV  # 현재 인접 노드들 구분
    visited[now] = True
    result.append(now)
    stack.append(now)
    #헷갈리지 않기 위해 현재와 다음을 구분

    while stack: #stack에 값이 있을떄만 돌아가도록 만든다.
        for next in graph[now]: #현재 now의 인접노드들을 기준으로 -> 6에 인접노드는 없기 때문에
            if not visited[next] :
                stack.append(now) #stack에 추가해준다. -> 다음을
                #왜 또 추가하지..?
                now = next #다음 인접 리스트들을 탐색하기 위한 now를 재설정해준다.
                visited[now] = True #방문을 확인시켜주고
                result.append(now) #방문이 완료되었으니 result에도 추가를 해준다.
                break #next가 여러개가 나올 것인데 그 중 1개만을 먼저 검토하고 지정할 것
                #또 검증이 완료된 것이라 break가 뜰 것 같은데
        else :
            now = stack.pop()
                #pop을 하고 pop에 대한 인접 노드를 다시 확인해야 함
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

