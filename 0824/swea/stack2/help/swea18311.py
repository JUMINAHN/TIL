import sys

sys.stdin = open('../input18311.txt')
#테스트 케이스 개수

def DFS(startV, endV, adj_list): #첫번쨰 정점 & 마지막 정점의 개수, 인접 리스트 받아오기
    visited = [False] * (endV+1) #+1을 하는 이유는 0번 idx는 사용하지 않기 떄문에
    visited[startV] = True #첫번쨰 정점은 방문을 하기 떄문에
    stack = []
    now = startV #현재 값
    result = [] #방문 경로 기록
    result.append(startV)

    #endV가 아니면..
    #인접노드기반으로 확인을 해야함
    #인접 노드는 어떻게 받아오는가..? => adjList를 매개변수로 받아와야하는가?
    flag = True
    while flag:  # 탐색이 끝날 때까지 반복
        for next in adj_list[startV]:  # 현재 노드의 인접 노드들을 순회              ::: (예를들면) startV에 2,3이 들어있다 --> 그럼 break로 끝낫으니 다시 여기로 오고 2의 인접노드로 출발..?
            if visited[next] == False:  # 방문하지 않은 인접 노드를 찾으면            ::: 먼저 2를 시작
                stack.append(now)  # 현재 노드를 스택에 저장 (백트래킹을 위해)
                now = next

                visited[next] = True  # 다음 노드를 방문 처리
                result.append(next)  # 결과 리스트에 다음 노드 추가                   :::2를 추가
                break  # 인접 노드를 찾았으므로 for 루프를 종료하고 다음 깊이로 이동 --> 여기 확인             ::::2를 추가하고 그냥 끝인 것?

        else:  # for 루프가 break 없이 끝났다면 (모든 인접 노드를 방문했다면)
            if stack:  # 스택이 비어있지 않다면
                now = stack.pop()  # 이전 노드로 돌아감 (백트래킹) --> 여기 확인인
                # now = stack.pop()을 통해 이전 위치로 돌아감으로써, 아직 탐색하지 않은 다른 경로를 찾아 나설 수 있습니다.
            else:  # 스택이 비어있다면
                break  # 모든 탐색이 끝났으므로 while 루프 종료

T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split()) #정점의 개수와 간선의 개수
    arr = list(map(int, input().split())) #간선의 개수만큼 연결된 두 정점
    #인접 리스트 만들기
    #간선 노드 개수만큼
#    adj_list = [0] * E
    #칸을 비워넣을 수 있따 [], 그럼 원하는 간선만큼 나온다.
    adj_list = [[] * E for _ in range(V+1)] #간선별 개수만큼 0번 idx는 사용하지 않기 떄문에, 간선 개수만큼
    # V1이 들어간 것, V2가 들어간 것
    # V1와 V2적절하게 어떻게 넣으면 좋을까..?
    for i in range(E): #연결된 두 정점 -> 간선의 개수만큼 순회 : 왜냐면 정점의 두개를 연결할거니까
        V1, V2 = arr[i*2], arr[i*2 + 1]
        adj_list[V1].append(V2)
        adj_list[V2].append(V1)
        # adj_list[V1].append(V2)
        # adj_list[V2].append(V1)
#    print(adj_list)

    #시작정점은 1로 시작한다.
    DFS(1, V, adj_list)