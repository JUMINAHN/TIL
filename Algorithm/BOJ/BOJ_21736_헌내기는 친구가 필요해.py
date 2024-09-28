# 재귀 DFS로 P에 접근해서 친구를 카운트 하면된다 -> 이코테의 얼음틀 로직으로 접근해보면 될 것 같은 문제
# 먼저 구조적으로 접근해보자 -> 어 그런데 -> X를 만나니까 BFS가 더 적합한 것 같다. -> 흠..
# 아니다 DFS로 할 수 있음
import sys
sys.setrecursionlimit(10**6) #recursion error로 백준에서 추천한 범위

# 왜 못날까?? -> people을 자체적으로 내부에서 선언해서 반환함
def DFS(row, col):  # 결과 값을 담아서 전달 -> 여기서 상하좌우 인접 노드 탐색
    people = 0
    # 범위가 벗어나는지 먼저 확인한다.
    if not (0 <= row < N and 0 <= col < M):  # 범위가 아니라면
        return 0  # 더해줄 것이니까 -> 그만할것
    # 그게 아니라 일단 i를 만낫다면 -> 즉 X만 아니라면
    if campus[row][col] != 'X':
        # 방문 처리하기 전에 만약 그 값이 P라면?
        if campus[row][col] == 'P':
            people += 1  # 만난 사람이 있따는 것을 더해준다.
        campus[row][col] = 'X'  # 방문 처리하고
        # 관련해서 DFS탐색 진행
        people += DFS(row - 1, col)
        people += DFS(row + 1, col)
        people += DFS(row, col - 1)
        people += DFS(row, col + 1)
        return people
    return 0


# N,M은 행과 열
N, M = map(int, input().split())
# 그것을 기반으로 campus를 채운다.
campus = [list(input()) for _ in range(N)]  # 하나의 덩어리로 들어갈 것 -> split할 필요없음 : int가 아님
# 시작 점 찾기 -> 초기값 설정
start_row = 0
start_col = 0
flag = True
for row in range(N):
    for col in range(M):
        if campus[row][col] == 'I':
            start_row = row
            start_col = col
            flag = False
            break  # col 종료
    if flag == False:
        break  # flag 빠져나가기
# print(start_row)
# print(start_col) #맞게 나오는 것 확인
result = DFS(start_row, start_col)  # result 결과 값을 담아서 전달
if result == 0:  # 아무런 사람도 못만낫다는 뜻이니까
    print('TT')
else:
    print(result)

'''
#I는 지금위치 
#0의 공간으로만 이동하고 X를 만나면 뒤돌아가는형식 == stack.pop()
    #즉 X에 갇힌 p는 계산할수없음
#P를 만나면 전체 토탈 카운트는 total += 1

#일단 i는 상하좌우로 이동할 수 있음 == 델타처럼 대각선도 이동할 수 있고,단 이문제는 델타가 아님
    #1. 일단 위-아래/좌-우로 이덩할 수 있음 : 이동경로
    #2. X만나면 되돌아가야함 -> stack에서 pop하기? (X를 넘어서 이동할 수 없음) 
    -> pop하고 그 위치에서 방항 전환 : 왔던길 굳이 갈 필요없으니까 
    -> 델타마냥 범위를 설정해주는 것(현재 위치 설정 반영) -> 끝점을 기반으로 다시 경로 탐색
    3. P만나면 토탈 +1하기
    4. 왔던길 돌아갈 수 없기 때문에 헨젤과 그레텔마냥 x로 다시 메꿔줌

#달팽이로만 방향 전환을 해서 감이 잡히진 않음
'''

'''
#DFS를 먼저 찍어보자
#아이디어 구상중
def DFS(startv, endV):
  visited = [False] * (endV+1)
  stack = []
  result = []
  now = startV
  stack.append(now)
  visited[now]
  result.append(now)

  while stack :
    now = stack[-1]
    for next in graph[now]:
      if not visited[next]:
        stack.append(next)
        visited[next] = True
        result.append(next)
    else :
      #pop할때도 필요없는 경로
      #해당경로 과자놓기
      arr[row][col] = 'X' #이걸 어떻게 활용할것인가..?
      stack.pop()
'''
