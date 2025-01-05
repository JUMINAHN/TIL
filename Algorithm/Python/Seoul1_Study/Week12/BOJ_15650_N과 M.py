#아이디어 -> pt요청

N, M = map(int, input().split()) #N까지, M개
result = [] #출력값을 담을 곳
visited = [False] * (N+1) #0은 포함되어 있지 않기 떄문에 -> 방문 확인이 필요
start = 1

def recur(num, start): #이게 height -> 높이라고 생각하면 된다.
    if num == M :#and result[1] > result[0]: #M일 떄 ->? 조건 -> 근데 이건 개수가 지정되어있을떄만
        print(" ".join(map(str, result))) #result의 값을 출력한다. -> 즉 result의 값이 2개
    #이전

    #그게 아니면 인접노드
    #이 코드는 첫번째보다 커야한다.
    #즉 1부터 N까지가 아니라,, -> 이것도 계속증가해야할 듯?
    #1부터가 계쏙 증가하면 될 것 같은데
    #num을 하니까 num의 최대가 2까지뿐이라서 안됨,,
    for i in range(start, N+1): #1부터 시작되니까 1, 2, 3, 4
        if not visited[i]: #단순히 앞에 것
            visited[i] = True
            result.append(i) #1을 방문으로 추가하고
            #1을 추가하고 -> 방문하지 않은 것 -> num이 총 2가 되니까 다시돌아오고 -> 다시 13
            recur(num+1, i+1) #num을 계속해서 증가시킨다 -> 일단 중복되면 안된다는 것 참고하기
            visited[i] = False #-> 방문은 체크
            result.pop() #pop을 해준다.
            #0에서 1시작 -> 그래서 다시 돌아가는.. 그럼 pop을 ㅏㅁㄱ아?
            #1에서 2시작 해서
#start = 0
recur(0, 1) #0번쨰 노드에서 시작

"------------------------------------------"
# # 이 코드는 첫번쨰 인자랑 중복이 아닌 것..
# N, M = map(int, input().split()) #N까지, M개
# result = [] #출력값을 담을 곳
# visited = [False] * (N+1) #0은 포함되어 있지 않기 떄문에 -> 방문 확인이 필요
#
# def recur(num): #이게 height -> 높이라고 생각하면 된다.
#     if num == M: #M일 떄
#         print(" ".join(map(str, result))) #result의 값을 출력한다. -> 즉 result의 값이 2개
#
#     #그게 아니면 인접노드
#     for i in range(1, N+1): #1부터 시작되니까 1, 2, 3, 4
#         if not visited[i]:
#             visited[i] = True
#             result.append(i) #1을 방문으로 추가하고
#             #1을 추가하고 -> 방문하지 않은 것 -> num이 총 2가 되니까 다시돌아오고 -> 다시 13
#             recur(num+1) #num을 계속해서 증가시킨다 -> 일단 중복되면 안된다는 것 참고하기
#             visited[i] = False
#             result.pop() #pop을 해준다.
#
# recur(0) #0번쨰 노드에서 시작