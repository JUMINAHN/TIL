import sys

sys.stdin = open('input4861.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #어느 방향에서 읽어도 같은 문자열을 회문
    # N크기의 글자판에서 길이가 M인 회문을 찾아 출력 -> 회문은 1개가 존재 (가로 or 세로)
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)] #길이 다 넣고

    #이제 탐색한다.
    #이동도 한다.
    #주의할 점은 row는 모두 돈다는 것 col의 위치만 바뀌는 것
    result = 0
    for row in range(N):
        for i in range(0, N-M+1):
            data = []
            for col in range(i, i+M):
                data.append(arr[row][col])
            if data == data[::-1]:
                #같을 경우 회문
                result = data
                break
        if result != 0:
            break
    if result == 0:
        arr2 = list(map(list, zip(*arr))) #전치행력
        for row in range(N):
            for i in range(0, N - M + 1):
                data = []
                for col in range(i, i + M):
                    data.append(arr2[row][col])
                if data == data[::-1]:
                    # 같을 경우 회문
                    result = data
                    break
            if result != 0:
                break
    print(f'#{tc}', end=' ')
    print("".join(map(str, result)))
