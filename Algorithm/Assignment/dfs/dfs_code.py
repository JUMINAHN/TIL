# 연습문제3
# 연결되어 있는 두개의 정점 사이의 간선을 순서대로 나열
# 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오
# 시작 정점 1
'''
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
### 다 탐색하자! (완전탐색)
def DFS(s, V):          # s 시작정점, V 정점개수(1번부터인 정점의 마지막 정점)
    visited = [0] * (V+1) # 방문한 정점을 표시
    stack = []          # 스택생성
    visited[s] = 1      # 시작정점 방문 표시

    now = s               # v 현재 정점
    while True:
        for next in adjL[now]: # now에 인접하고, 방문안한 next가 있으면
            if visited[next] == 0:
                stack.append(now) # push(now) 현재 정점을 push하고
                now = next           # next에 방문
                print(now)
                visited[next] = 1  # next에 방문 표시
                break           # for next, now부터 다시 탐색 남은 갈림길을 두고
        else:               # 남은 인접정점이 없어서 break가 걸리지 않은 경우
            if stack:       # 이전 갈림길을 스택에서 꺼내서 if TOP > -1
                now = stack.pop()
            else:           # 되돌아갈 곳이 없으면 남은 갈림길이 없으면 탐색종료
                break       # while True # 스택이 비어있으면? => 되돌아갈 길이 없; 탐색 불가


# Testcase
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V: 마지막 정점 번호 or 정점 개수 (정점이 0부터 시작하면 마지막 인덱스 변동있음)
    adjL = [[] for _ in range(V+1)] # 비어있는 인접리스트. V번까지 존재해야하므로 V+1. 정점 7개면 adjL[7]까지 있어야 함
    arr = list(map(int, input().split()))

    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2) # 이것만 작성하면 한쪽 연결만 나옴 => [[], [2, 3], [4, 5], [7], [6], [6], [7], []]
        adjL[v2].append(v1) # 이것까지 해줘야 연결된 모든 정점 연결

    print(adjL) #  0     1         2        3       4       5         6         7
    # 인접 표현 : [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
    # adjL[0]은 사용안함. adjL[1]은 1에 인접한 정점


DFS(1, V)

