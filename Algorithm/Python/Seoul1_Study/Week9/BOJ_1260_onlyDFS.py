#정점 번호가 더 작은 것을 방문하고, 더 이상 방문할 점이 없는 경우 종료
#정점 노드는 1번부터 N번까지이다.
#정점의 개수 N개, 간선의 개수 M개, 탐색을 시작할 정점 번호 V가 주어진다.
#각 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. == 양방향이다.


#예제 입력1, 입력3 케이스는 맞게 나온다.
def DFS(startV, endV): #시작노드, 끝노드
    stack = []
    visited = [False] * (endV+1) #끝노드 +1 정점 노드 개수만큼
    result = [] #결과 값을 담을 곳

    now = startV
    stack.append(now) #stack에 담고
    visited[now] = True #visited에 당고
    result.append(now) #result에 담아서

    while stack: #stack에 있을동안
        now = stack[-1] #마지막 stack에 있는 값 기준
        for next in adjList[now]:
            if not visited[next]:
                stack.append(next)
                visited[next] = True
                result.append(next)
                break
        else :
            stack.pop()
    return result

N, M, V = map(int, input().split()) #정점의 개수 N개, #간선의 개수 M개, 탐색 시작할 정점 번호
#간선의 개수만큼 input을 받는다.
#인접 리스트 생성 -> 정점의 개수 + 1개만큼
adjList = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split()) #노드1, 노드2
    adjList[v1].append(v2)
    adjList[v2].append(v1) #각 idx에 맞는 node 입력
#print(adjList) #[[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
#2차원 자체에 솔트를 하면? == 값이 이상해진다.
# adjList.sort()
# print(adjList)

#그렇다면 배열로 순회를 해서 각 노드를 정렬한다면? == 원하는 의도로 나올 것 같긴함
for adj in adjList:
    adj.sort()
#print(adjList)

result = DFS(V, N) #dfs 방문 순서
print(result)