import sys

sys.stdin = open('input4871.txt')

T = int(input())
for tc in range(1, T+1):
    def DFS(s, G):
        visited = [False] * (G + 1)
        stack = []
        visited[s] = True
        now = s

        while True:
            for next in adjL[now]:
                if visited[next] == False:
                    stack.append(now)
                    now = next
                    # print(now, end = ' ')
                    visited[next] = True
                    return
            else:
                if stack:
                    now = stack.pop()
                    print(1)
                else:
                    print(0)
                    return

    V, E = map(int, input().split())  # 정점의 개수, 간선의 개수 -> 0 존재 x
    arr = [list(map(int, input().split())) for _ in range(E)]
    s, G = map(int, input().split())
    adjL = [[] for _ in range(V + 1)]  # 몇개..

    # 노드 연결->짝은 이미 설정했으니까 나눌 필요는 없고
    # 바로 append해주면 될 것 같음
    for i in range(E):  # 양방향이 아니라 단 방향임-> 노드 연결
        adjL[i].append(arr[i])

    print(f'#{tc}', end = " ")
    DFS(s, G)  # 정점 개수, 마지막 노드 개수
