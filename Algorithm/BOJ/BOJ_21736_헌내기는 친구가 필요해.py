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