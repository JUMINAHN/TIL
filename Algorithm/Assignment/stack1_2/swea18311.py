import sys

sys.stdin = open('input18311.txt')

def dfs(startV, endV, adj_list): #정점 노드의 개수보다 1이 더 많아야 함 -> 그 이유는 0부터 시작하지 않기 떄문에
    visited = [False] * (endV+1)
    visited[startV] = True #일단 방문을 했고,

    result = []
    result.append(startV) #현재 방문 경로 표시 -> 출력
    now = startV #지금 내가 있는 위치 표시

    stack = [] #왔던 경로를 메모하기 위함
    while True: #인접 리스트들을 방문 할 것
        for next in adj_list[now]: #현재 인접리스트를 기준으로 방문확인 할 것
            if visited[next] == False: #인접 노드에 방문하지 않았을 때 방문을 할 것, 다음것에 대한 예를들면 2,3이다
                #그럼 방문 기록을 할 것
                stack.append(now) #이전에 방문한 곳을 기록
                now = next #다음 방문을 True
                visited[now] = True
                result.append(now) #새로 방문한 곳 기록할 것 #2가 append되고, 3에 대한 것은 하지 않는다.
                #왜냐면 인접 노드 기준으로 그럼 -> adjlist 2와 관련된 것을 또 넣는다
                break
        #여기서 for-else 구문을 사용하는게 keypoint -> ?
        else: #만약 모두 방문을 했다면?
            if stack: #stack에 값이 있다면, 아직 back을 하지 않았다는 것
                now = stack.pop() #방문했던 곳 pop, 그리고 왔던 경로로 표기 -> 다음것도 방문했었는지 확인을 위해서
            else: #stack이 없다면 모든 경로를 탐색하고 집으로 돌아왔다는 뜻 == 끝
                break
    return result


#테스트 케이스 개수
T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split()) #정점의 개수와 간선의 개수
    arr = list(map(int, input().split()))
    #단 정점의 개수 + 1을 해줘야함, 그 이유는 정점의 노드가 1부터 시작하기 때문에, 첫 칸은 비워둘 것
    adj_list = [[]  for _ in range(V+1)] #인접 리스트 -> 생성, 몇 칸인지는 모르나 정점의 개수 기반으로 확인하기
    #이제 받은 arr을 기반으로 인접리스트 생성 필요
    for i in range(E) : #간선의 개수기반으로 V1,V2확인하기 : 정점 1 정점 2 --> 2 * 7을 한 것이 총 정점 arr의 개수
        v1, v2 = arr[i*2], arr[i*2 + 1] #list안에는 반드시 integer가 들어가야 함 list는 안돼 -> 인접리스트의 내용을 담는 것이 아님. arr의 값
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
    #인접 노드 생성
    result = dfs(1, V, adj_list) #시작 노드, 끝 노드, 인접 리스트 전달
    print(f'#{tc}', end = " ")
    for i in range(len(result)):
        if i == len(result) - 1:
            print(result[i], end = "")
        else :
            print(f'{result[i]}-', end="")
    print()
