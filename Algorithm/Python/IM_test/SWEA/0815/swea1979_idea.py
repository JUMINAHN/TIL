import sys

sys.stdin = open('input1979.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) #가로세로길이 N, 단어길이 K
    puzzle = [list(map(int, input().split())) for _ in range(N)] #puzzle에 값을 채워넣기
    #전체 count가 3이면 1씩 채워넣기
    #행-열의 visited를 2개만들어서 행/열이 3개이면 전체에 total +1 을 시키자
    #visited는 N개씩 만들면 된다.
    visited = [[0] * N for _ in range(2)] #2개를 만드는 이유는 행/열
    #visited는 count의 일종이다.
    #헷갈리면 일단 넣자
    #count 0과 1할때 처럼 넣으면 되는데..
    for row in range(N):
        for col in range(N):
            if puzzle[row][col] == 1:
                visited[0][row] += 1 #row에 대한게 가로마다 누적됨
                visited[1][col] += 1 #col에 대한게 세로마다 누적되고
    print(visited[0]) #row
    print(visited[1]) #col
    print('-----')
    #visited로 풀수 없는게 총 4개인게 4개라고 보장될 수 없기 떄문에 -> 성립되지 않는다.
    #이 방법은 잘 알아둘 것
    #visited[0][p] += 1 #ist indices must be integers or slices, not list
    print('c', visited)
