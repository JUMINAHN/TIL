import sys

sys.stdin = open('input6485.txt')
T = int(input())
for tc in range(1, T+1):
    #0. 삼성시에는 버스 정류장이 5000개 있고 1부터 5000까지 번호가 붙어져 있다.
    bus_stop = [i for i in range(1, 5001)]
    #print(bus_stop)

    #1. 버스노선 N개
    N = int(input())
    #2. Ai~Bi, 노선별 방문하는 버스 정류장의 위치
    route = []
    for _ in range(N):
        A, B = map(int,input().split()) #범위 A부터 B까지
        route.append([A,B])
    #3. P개의 버스 정류장 : Ai~Bi,에서 노선별 방문하는 버스 정류장의 위치와 관련되어 있음 ->bus stop과 관련
    P = int(input())
    #4. P개의 버스 정류장 번호 -> 해당 번호에 counting
    c = [] #버스정류장 번호
    # for bus in bus_stop: #idx가 들어갈 것
    #     if bus == int(input()):
    #         c.append(bus)

    for _ in range(P):
        c.append(int(input()))

    #방문 확인을 위한 list 생성
    #c와 대조해서 위치 확인하면 됨 #c가 필요없을수도 있음..
    visited = [0] * 5001 #버스노선도 때문에

    #route내부를 돌면서 for에 range별로 돌고 visited 위치에 +1
    for i in range(N): #노선 개수
        for r in range(route[i][0], route[i][1]+1): #노선 하나씩 추출 r에 1부터 3까지의 숫자 -> 어짜피 입력되는 값들 보다 idx가 작게 들어간다.
            visited[r] += 1 #내가 원하는 위치에 +1을 해주자
    print(f'#{tc}', end = ' ')
    for i in range(c):
        if i == 0:
            continue
        print(visited[i], end = ' ')





    #print(route)
    #print(c)