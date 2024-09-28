#2024-09-28
'''
4 5
00110
00011
11111
00000
'''
#코드를 이해한 내용을 바탕으로 작성해보기
#왜 DFS를 사용해야하는가?
#인접노드들을 끝까지 탐색해봄으로써 영역을 명확하게 구분할 수 있음

#방문 처리는 0과 1로 -> 아이스 틀에 대한 것으로 진행을 하고,
#stack은 필요없음 == DFS 재귀 구조로 이루어질 것이기 떄문에
def DFS(row, col): #행 -> 열로 나누어 접근해야 하기 떄문에
    #먼저 범위를 벗어나는지에 대한 확인이 이루어져야 함
    #범위를 벗어나면 재귀 구조가 끝나는 것
    if not (0<=row<N and 0<=col<M): #해당 영역이 아니라면 ==> TypeError: '<=' not supported between instances of 'int' and 'list'
        return False #그냥 거짓 -> 더이상 진행하지 않겠다는 것
    #그리고 그게 0이라면
    #1인지 아닌지, 얼음틀의 영역인지 아닌지에 대한 구분이 선행되어야 함
    if ice[row][col] == 0: #방문 표시를 진행하자 -> 방문을 진행
        ice[row][col] = 1 #1을 대입해서 추후 다시 못가도록 하고
        #상하 좌우에 대한 탐색을 다시 진행한다.
        DFS(row-1, col) #상
        DFS(row+1, col) #하
        DFS(row, col-1) #좌
        DFS(row, col+1) #우
        return True #참이니까 계쏙 진행을 하고
    return False #끝이 난 것을 반환


#먼저 관련해서 input을 받아서 얼음틀을 채워보자
#N과 M이 주어진다.
N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)] #M만큼 -> 값이 들어갈 것

#얼음틀을 채웠고, 그 얼음틀에서 내가 찾는 것이 있는지 확인하자 : 같은 인접노드인지 확인하는 것
icecream = 0
for row in range(N):
    for col in range(M): #한개씩 주변 노드의 유무를 탐색하는 것
        #즉 DFS 자체 내부에서 상하좌우 경로 탐색이 더 이루어져야 함
        #0을 발견하고 말고에 따라서 이루어 지는 것 -> 즉 0이 발견되었는가
        if DFS(ice[row], ice[col]) == 0: #이거를 살려보고 -> 이게 진짜면 icecrea 생성이 가능한 것 -> True / False임에 따라서
            icecream += 1 #icecream 생성

print('result =', icecream)
