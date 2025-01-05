import sys
#흠.. 일단 pass

sys.stdin = open('input1961.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #90, 180, 270 회전한 모양을 구하라
    N = int(input()) #행의 개수
    arr = [list(map(int, input().split())) for _ in range(N)]
    #arr 회전한 것들 한줄씩 출력

    result_turn = []
    turn90 = []
    result_turn.append(turn90)
    for col in range(N):
        for row in range(N-1, -1, -1):
            turn90.append(arr[row][col])

    turn180 = []
    result_turn.append(turn180)
    for row in range(N-1, -1, -1):
        for col in range(N-1, -1, -1):
            turn180.append(arr[row][col])

    turn270 = []
    result_turn.append(turn270)
    for col in range(N-1, -1, -1):
        for row in range(N):
            turn270.append(arr[row][col])

    print(result_turn)
    # for a, b, c in result_turn:

