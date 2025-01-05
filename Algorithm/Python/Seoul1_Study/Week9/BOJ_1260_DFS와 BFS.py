#DFS와 BFS 탐색 결과를 출력하는 프로그램 생성
#방문 정점이 여러개인경우 정점 번호가 작은것 우선 방문할 수 있도록 진행
#간선은 양방향
from collections import deque

#DFS먼저 코드 작성
def DFS(startV, endV):
    visited = [False] * (endV+1)
    stack = []
    result = []
    now = startV
    stack.append(now)
    visited[now] = True
    result.append(now)

    while stack: #stack이 빌때 까지
        now = stack[-1] #pop을 생각 -> 인접 노드가 있을떄, 없을떄를 생각하자
        for next in adjList[now]: #다음 인접노드가
            if not visited[next]: #방문하지 않았다면
                stack.append(next)
                visited[next] = True
                result.append(next)
                break #한 군데 기준으로 계속 깊이 파고들 것이니까
        else : #단 인접 노드가 없다면
            stack.pop()
    return result

#BFS 코드 작성 == dequeu 활용
def BFS(startV, endV):
    visited = [False] * (endV+1)
    queue = deque()
    result = []
    now = startV
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

N, M, V = map(int, input().split()) #정점 개수, 간선 개수, 시작할 정점 번호
#인접 리스트 생성 -> 노드 개수 + 1만큼
adjList = [[] for _ in range(N+1)] #만큼 생성
#input으로 받아와서 adjList에 걸맞게 배분을 해준다.
for _ in range(M): #간선 개수만큼 input됨
    v1, v2 = map(int, input().split())
    adjList[v1].append(v2)
    adjList[v2].append(v1)
#print(adjList) #맞는지 확인인
#작은 것 부터 우선 방문할 수 있도록 설정
for a in adjList:
    a.sort() #정렬해준다.
result1 = DFS(V, N) #시작 노드 정점 노드
result2 = BFS(V, N)
print(*result1)
print(*result2)

# 완료!