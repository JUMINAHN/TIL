import sys

sys.stdin = open('input18311.txt')

def DFS(s, V): #시작하는 정점의 값, 노드의 개수 -> 내가 원하는 정점들이 방문했는지 확인 필요
    visited = [False] * (V+1)
    stack = []
    visited[s] = True #방문 함
    now = s #현재의 값 구별


    global result #될라나
    result = []
    result.append(now)

    while True:# 다음 노드
        for next in adjL[now]: #현재의 idx에 들어있는지 인접노드들
            if visited[next] == False: ##여기서 문제 발생함 --> 현재의 값을 기준으로 하니까 변경 된 값에서 현재로 대입
                stack.append(now) #현재 값
                now = next

                result.append(next)
                #print(now, end = ' ')
                visited[next] = True
                break
        else :
            if stack :
                now = stack.pop()
            else :
                break

T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())
    #간선의 개수만큼 연결된 두 정점
    arr = list(map(int, input().split()))#노드, 정점 1~V개 까지 --> 0까지 포함되어서 +1을 해준다.
    #인접한 노드 구하기
    adjL = [[] for _ in range(V+1)]
    #인접한 노드에 값채우기 -> 두짝식 나눠서 넣기 -> 간선의 개수만큼 짝 지우기
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2) #1개의 idx에 넣을 값
        adjL[v2].append(v1)

    DFS(1, V) #가장 작은 값, 가장 큰 값값
    print(f'#{tc} {"-".join(map(str, result))}')