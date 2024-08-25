#A와 B는 99으로 고정 -> 정점의 개수는 최대100개, size가 100인 정적 배열을 선언
#되돌아갈 수 없음, 양방향 노선이 아님
#정점은 출발/도착점 제외 98개를 넘어가지 않음, 한개의 정점에서 선택할 수 있는 길의 개수도 2를 넘어가지 않음
#정점의 max는 2개

import sys
sys.stdin = open('input1219.txt')

def dfs(startV, endV, adj_list):
    visited = [False] * (endV+1) #100개 만들기 -> 총 100개
    visited[startV] = True

    stack = []
    now = startV

    while True: #while loop때문에 중간에 빠져나가지 못할 것
        for next in adj_list[now]: #현재 노드를 기준으로 다음 방문할 노드
            #만약 방문하지 않은 곳이었는지 확인해야 함
            if next == endV: #똑같으면 : 찾을 위치를 찾게 되면
                visited[next] = True
                return next #지금 위치 반환해

            if visited[next] == False:
                stack.append(now)
                now = next
                visited[now] = True
                break
        else : #모든 노드를 방문했다고 가정했을떄
            #돌아올 곳이 있다면?
            if stack: #나의 현재위치를 반환해서 해당 내용을 기반으로 다시 탐색하자
                now = stack.pop()
            else :
                break #끝
    return now

#테스트 케이스 개수
T = 10
for tc in range(1, T+1): #예시에 따르면 0 1 3 7 99 끝
    test_case, E = map(int, input().split()) #E == 길의 총 개수 (간선의 개수)
    arr = list(map(int, input().split()))
    V = 99 #마지막 정점 노드
    adj_list = [[] for _ in range(V+1)] #정점의 노드 개수만큼
    #arr에 있는 것을 adj_list에 copy

    for i in range(E): #생각해보니까 간선의 개수만큼임 -> input되어 있는 만큼 진행되어야 하기 떄문에
        v1, v2 = arr[i*2], arr[i*2 + 1]
        adj_list[v1].append(v2)
    #print(adj_list)

    result = dfs(0, 99, adj_list) #시작노드, 끝노드, 인접 리스트
    if result == V:
        print(f'#{test_case} 1')
    else :
        print(f'#{test_case} 0')

