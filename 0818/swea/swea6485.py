import sys

sys.stdin = open('input6485.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #1. 삼성시 5000개 버스 정류장 -> 1에서 5000번까지 붙어있음
    visited = [0] * 5001
    #2. 버스노선 : N개, i번쨰 버스 노선 : Ai~Bi의 모든 정류장을 다님
    N = int(input())
    bus_stop = []
    for _ in range(N):
        AB = list(map(int, input().split())) #A부터 B까지
        bus_stop.append(AB)
    #3. P개의 버스 정류장에 대해 몇 개의 버스 노선이 다니는지 구하기
    P = int(input()) #버스 정류장 개수 --> 들리는 버스 정류장 5000개 중에서
    #4. j번째 정수는 버스 정류장을 지나는 버스 노선의 개수 --> 5000개 중에 들리는 버스 정류장 개수
    # visitied중에서 해당되는 정류장의 값 가져오기
    bus_position = []
    for _ in range(P):
        bus_position.append(int(input()))

    #어느 정류장에 들렸는지 개산하기
    for stop in bus_stop: #A와 B
        for i in range(stop[0], stop[1]+1):
            visited[i] += 1 #busstop에 들리는 것

    print(f'#{tc}', end = ' ')
    for bus in bus_position:
        print(visited[bus], end = ' ')
    print()


