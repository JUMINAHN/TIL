#DFS 이해를 위한 코드 작성해보기 하기는 테스트 케이스
'''
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def DFS(s, V): #시작 노드 / 정점의 개수 --> 1부터 ~ V까지 (즉 마지막 V)
    #그 전에 나의 시작노드의 방문 여부를 알기위해서 visited를 선언하고, stack을 통해 들어갔다가 나오는 것을 확인한다.
    visited = [False] * (V+1) #정점의 개수만큼 --> False는 아직 방문하지 않음을 의미한다.
    stack = []
    visited[s] = True #첫번째는 방문을 한 것이니 -> 방문을 했음을 표기한다.
    now = s #그대로 해도 되지만, 헷갈릴 수 있기 떄문에 구분

    #여기서 방문을 하고, 또 다음 인접 노드에 방문을 하게 되면 나의 현재값을 기록하는 행위를 할 것이다.
    #그러기 위해선 전체를 먼저 순환해야 한다.
    while True:
        for next in adjL[now]: #예를 들면 1번쨰 idx에는 2,3이 next 노드임을 알 수 있고, 그걸 기반으로 접근
            if visited[next] == False: #아직 방문하지 않았다면 --> 2번쨰 노드가
                stack.append(now) #이전 값
                now = next #다음 값을 현재에 넣어야 함 ########이 부분 확인 실수
                print(now, end = ' ')

                visited[next] = True #다음의 방문을 나타내는 것
                break
        else :
            if stack : #그게 아니라 모두 순환을 하고, 즉 모든 노드를 지나쳐 와도 stack에 남아 있는 경우라면
                now = stack.pop() #남아 있는 애들을 pop해주고 --> 이걸 다시 now 값으로 담아야 함 -> pop한 곳에서 다시 접근해야 함 ####이 부분 실수
            else:
                break #그게 아니라면 나온다.

#DFS를 차근 차근 접근해보자
#먼저 정점개수와 간선개수를 받고, input으로 arr 배열을 입력받는다.
V, E = map(int, input().split())
arr = list(map(int, input().split())) #1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
adjL = [[] for _ in range(V+1)] #간선과 인접된 list를 idx를 기반으로 나누어준다. -> 빈 배열에 인접된 리스트를 담을 것

#인접된 list를 담기 위해서 간선 개수를 기반으로 arr을 돌자
#짝을 맞추기 위해서 2배임을 인지하고 코드를 작성
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    #간선 2개로 나눈 것을 양방향으로 연결해주기 위해서 [0] 순서 idx 즉 노드 번호를 기반으로 들어갈 값을 append 한다.
    adjL[v1].append(v2)
    adjL[v2].append(v1)

DFS(1, V) #시작 노드 정점 개수