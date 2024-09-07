import sys

sys.stdin = open('input6485.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #1. 1~5000의 버스 정류장 -> 총 5001개
    bus_stop = [0] * 5001
    #2. 버스 노선 N개
    N = int(input())
    #3. 버스 노선 Ni은 A~B의 정류장에 들린다.
    for _ in range(N):
        A,B = map(int, input().split())
        for i in range(A, B+1):
            bus_stop[i] += 1 #들렸음을 표시
    #4. P개의 정류장이 있다.
    P = int(input())
    #5. P개의 정류장 번호를 주고 그 곳에 대해서 몇 개의 버스가 가는지 => 버스 노선에 기반해서 몇 개가 가게 되는지
    check = [int(input()) for _ in range(P)]
    print(f'#{tc}', end = ' ')
    for i in range(P):
        print(bus_stop[check[i]], end = ' ')
    print()
