#단방향 그래프
#노드의 경로가 존재하는가?
import sys
sys.stdin = open('input4871.txt')

def dfs(startV, endV, adj_list):
    visited = [False] * (endV+1)
    visited[startV] = True
    now = startV

    stack = []
    while True :
        for next in adj_list[now]:
            if next == endV:
                visited[next] = True
                return endV
            elif visited[next] == False:
                stack.append(next)
                now = next
                visited[now] = True
                break
        else :
            if stack:
                now = stack.pop()
            else :
                break
    return now

#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) #정점의 개수 #간선의 개수
    arr = [list(map(int, input().split())) for _ in range(E)] #간선 개수만큼
    S, G = map(int, input().split()) #출발노드와 도착노드
    adj_list = [[] for _ in range(V+1)] #간선노드 +1
    #첫번째를 위치, 두번째를 인접노드로
    #간선의 위치를 기반으로 순회
    #원래 간선 개수만큼 순회.. -> 지금 arr에 개수자체가 6개가 들어있고 첫번째가 위치 두번쨰가 인접 노드
    for i in range(E):
        adj_list[arr[i][0]].append(arr[i][1]) #IndexError: list index out of range

    #노드번호는 1번부터 존재하며 마지막 끝 V에 도착하는 것이 목표
    result = dfs(S, G, adj_list) #출발 노드와 도착 노드
    #print(result)
    if result == G :
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')