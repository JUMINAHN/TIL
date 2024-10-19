#주석 없는 코드

N, M = map(int, input().split())
data = list(map(int, input().split()))
data = set(data)
data = list(data)
data.sort()

result = []
def recur(num):
    if num == M:
        print(' '.join(map(str, result)))
        return
    for i in range(len(data)):
        if not result or data[i] >= result[-1] :
            result.append(data[i])
            recur(num + 1)
            result.pop()
recur(0)
 
'------------------------------------------'
#주석 있는 코드
#
#N개의 자연수 중에서 M개를 고른 수열
#같은 수를 여러번 골라도 된다
#내림차순이다. -> 잘못봤다 비내림차순이다.
#문제를 다시 읽어보니까 같은 수 출력해도 됨 == 단 중복되는 것은 여러번 출력하면 안됨
#모르겠다..
#돌아왔다 = 이떄까지 썻던거 잘 정리만 했어도 나왔었을 듯.. 생각을 더 해보자


#한줄에 하나씩 문제의 조건을 만족하는 수열 출력 -> 중복되는 수열을 여러번 출력하면 안된다.
N, M = map(int, input().split())
data = list(map(int, input().split())) #4,4,2 -> 내림차순 정렬하기
data = set(data) #집합
data = list(data) #다시 리스트로 => 중복 제거
data.sort()

result = [] #결과 값 == 이것이 recur 값에 있으면 계쏙적으로 초기화 됨
#똑같은 것울 출력 해도 됨 -> 단, 보니까 자신 보다 작으면 안됨
def recur(num): #height라고 생각하면 됨
    if num == M: #height이면
        print(' '.join(map(str, result)))#결과 값 #map() must have at least two arguments. == ' '.join(map(str, *result)
        return #하는 이유?
        #RecursionError: maximum recursion depth exceeded in comparison
        #return 1 #0 => list index out of range
        #값이 증가하게 되니까 재귀에서 빠져나오지 못하는 것 같다
        #생각해보니까 set을 해서 N개가 아니다..
    for i in range(len(data)): #list형태로 출력할 것이기 때문에 => #0부터 2까지
        if not result or data[i] >= result[-1] : #result가 없거나 result의 마지막값보다 클 경우
            #i의 값이 증가하니까 -> recur로 i의 값을 전달할 것
            result.append(data[i]) #결과 값에 출력할 내용을 담음
        #그리고 재귀로 호출
            recur(num + 1) #num의 값도 증가해야함 == 이것을 고려하지 못함
        #하지만 -> pop을 하지 않으면 기하급수적으로 내용이 늘어남
            result.pop() #7을 넣었으면 출력하고 next
recur(0) #이미 위에서 출력


#data.sort(reverse=True)# 내림차순 정렬
#print(data) #== 내림 차순 확인 완료
#출력 값을 보면 -> 1을 뽑았으면 그 1은 건들지 못하고 그 뒤에 숫자들을 뽑을 수 있는 것 같다
#visited = [False] * (N) #방문 여부 확인을 위해서
#N+1을 하지 않는 이유는 data의 배열크기 만들 돌것이기 떄문에
# def recur(num): #시작 height
#     result = [] #result에 추가된 값 출력
#     if num == M: #높이가 같아지면
#         print(''.join(map(str, *result))) #출력
#     #그게 아니면 for문으로 하나씩 묶기
#     for i in range(0, N) : #data 인덱스 0부터 N-1까지
#         #그런데 방문을 확인해야 함
#         # if not visited[i]: #방문을 하지 않았다면
#         #     #방문을 한다
#         #     visited[i] = True #그리고 출력값에 추가한다
#         #     result.append(data[i]) #방문하지 않았으니 결과 값에 넣는다.
#         #     recur(num+1) #높이가 증가해야함 -> 깊이 증가
#         #     #방문이 되어있으면


