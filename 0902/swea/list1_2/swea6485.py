import sys
#삼성시 버스노선
#문제 이해에 많은 시간 소요
sys.stdin = open('input6485.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #방문 여부를 확인하기 위해서 visited 배열과 같은 원리로 작용 됨
    bus_stop = [0] * 5001 #1부터 5000번의 버스노선이 있기 때문에, count배열로 확인을 하기 위해서 배열 하나 선언
    N = int(input()) #버스 노선도 개수
    #버스 노선도 만큼 순회하고 해당 배열과 관련된 배열에 count
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        #해당 범위만큼 count하기 위해서
        for i in range(Ai, Bi+1): #B+1을 하는 이유는 B까지의 범위를 포함하기 위해서임
            bus_stop[i] += 1 #bus_stop에 해당 하는 idx의 count를 더해준다.
    #상기는 배열에 방문하는 노선도르 체크
    #내가 찾는 P 정류장과 관련된 데이터는 하기에서 진행
    find_stop = []
    P = int(input())
    for _ in range(P):
        find_stop.append(int(input()))#내가 찾고싶은 정류장 번호들 담고
    #배열에 내가 찾는 정류장 번호 바로 출력
    print(f'#{tc}', end= " ")
    for f in find_stop:
        print(bus_stop[f], end= " ")
    print()
