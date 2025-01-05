from collections import deque

def BFS(startV, endV):
    visited = [False] * (endV+1)
    queue = deque()
    result = []
    now = startV #시작 노드 확보
    queue.append(now)
    visited[now] = True
    result.append(now)

    while queue:
        now = queue.popleft()
        for next in adjList[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                result.append(next)
    return result

#방문할 수 있는 정점이 여러개인 경우 정점 번호가 작은 것을 먼저 방문 == BFS는 상관이 없음
#첫째줄에 정점 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V가 주어진다.
N, M, V = map(int, input().split()) #정점개수, 간선개수, 시작정점
#인접 노드들 구성
adjList = [[] for _ in range(N+1)] #정점 개수만큼만들어질 것
#input 받아서 adjList를 구성할 것
for _ in range(M): #간선 개수만큼 루프
    v1, v2 = map(int, input().split()) #v1, v2 input을 받음
    adjList[v1].append(v2)
    adjList[v2].append(v1) #인접 노드를 구성할 것
#print(adjList) #맞게 구성되어있는지 확인해보자 -> 순서대로 잘 들어가 있는 것을 볼 수 있음
#또 순서가 맞게 나오지 않기 떄문에 list별 sort 진행
for a in adjList:
    a.sort()
#해당 값을 기반으로 출력할 것
result = BFS(V, N)#시작노드, 끝노드
print(result)