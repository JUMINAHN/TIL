
#주석이 없는 코드
def dfs(visited, startV, adjList):
    visited[startV] = 1
    for i in adjList[startV]:
        if not visited[i] :
            visited[i] = 1
            dfs(visited, i, adjList)
    return visited

N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]
adjList = [[] for _ in range(N+1)]
for ar in arr:
    adjList[ar[0]].append(ar[1])
    adjList[ar[1]].append(ar[0])
visited = [0] * (N+1)
result = dfs(visited,1,adjList).count(1)
print(result-1)

'---------------------------------'

#주석이 있는 코드
#DFS로 풀면 좋을 것 같다
#그래프
#1번 컴퓨터로 웜 바이러스가 걸렸을 때 -> 1번을 통해 바이러스에 걸리는 컴퓨터의 수
#1번 컴퓨터를 통해 웜바이러스에 걸리게 되는 컴퓨터의 수
#오.. 한번만에 정답!

def dfs(visited, startV, adjList): #방문, startV, 인접리스트
    #재귀
    #stack = [] #이 안에 넣으면 재귀할때마다 값이 초기화..?
#    stack = []
#    stack.append(startV) #넣고
    visited[startV] = 1 #방문 처리
    for i in adjList[startV]:
        if not visited[i] : #방문하지 않았다면 -> 방문을 시키자
            visited[i] = 1
#            stack.append(i)
            dfs(visited, i, adjList)
            #재귀를 해야 함 == 현재 단순 stack.append만 하는 중
    return visited

N = int(input()) #node 개수
M = int(input()) #간선의 개수
#연결되어 있는 간선들
arr = [list(map(int, input().split())) for _ in range(M)] #간선의 개수만큼
#해당 간선을 기반으로 adjList==graph 생성
#print(arr)
adjList = [[] for _ in range(N+1)] #노드개수만큼 -> 0번 노드는 없음  => 총 8개가 있어야 함
for ar in arr: #arr하나씩 추출
    adjList[ar[0]].append(ar[1]) #인접리스트에 내용 추가
    #하나 더 추가해야 양방향
    adjList[ar[1]].append(ar[0]) #인접리스트에 내용 추가
    #adjList[ar[0]] = ar[1] #인접리스트에 값 추가
#print(adjList) #맞게 연결되어있는 것 확인 == [[], [2, 5], [3], [], [7], [2, 6], [], []]
#해당 내용을 기반으로 -> dfs 시작
visited = [0] * (N+1) #방문 노드 표시를 위함 ==> 방문하면 1로 만들 것
#dfs(visited,1,adjList) #시작노드는 1이니까 1을 넣어줌
#print(dfs(visited,1,adjList)) #지금 1이 있는 것들
result = dfs(visited,1,adjList).count(1) #1이 있는 것을 count
print(result-1) #왜냐하면 첫번쨰 1은 제외 == 1번을 통해 감염된 것을 구하기 떄문에

#따라서 총 1의 개수는?