import sys

sys.stdin = open('input5789.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #1번부터 N번까지 N개의 상자 -> 모두 0으로 설정
    #일정 범위의 연속한 상자를 동일한 숫자로 변경
    #i번쨰 작업에 대해 L번부터 R번을 i로 변경
    #현주가 Q회 동안 위의 작업을 순서대로 한 다음 N개의 상자에 적혀있는 값들을 순서대로 출력하는 프로그램

    #입력
    #N개의 상자, Q회동안 변경할 것 -> 공백으로 주어진다.
    N, Q = map(int, input().split())
    #상자 5개
    box = [0] * N
    #idx 범위 주의할 것
    for i in range(Q): #Q만큼 변경할 것 -> 1번 상자일 떄 -> 박스가 1부터 시작하니까 idx == 0
        L, R = map(int ,input().split())
        for j in range(L-1, R):
            box[j] = i+1
    print(f'#{tc}', end=' ')
    print(*box)