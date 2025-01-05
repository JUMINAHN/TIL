import sys

sys.stdin = open('input20397.txt')

# Testcase 수
T = int(input()) #Testcase만큼
# Testcase 만큼 반복
for tc in range(1, T+1):
    # 돌의 개수 N, 뒤집기 횟수 M
    N, M = map(int, input().split())
    # N개의 초기 상태 배열 arr
    arr = list(map(int, input().split()))
    # i번째 돌을 사이에 두고, 마주보는 j개돌에 대해 같은 색이면 뒤집고 다른 색이면 그냥 둔다.
    for _ in range(M): #M번 만큼 뒤집기를 진행한다.
        #기준 standard, 바뀔 범위 R
        standard, R = map(int, input().split())
        #헷갈리니까 일단 standard의 내부 값을 맞춰주자
        standard = standard - 1
        #기준을 기반으로 범위만큼 순회
        for i in range(1, R+1): #0을 더할 필요가 없기 떄문에 1부터 시작하고 count를 진행한다.
            #마주 보는 돌을 비교해야 한다.
            #단 standard가 input받아지는 것은 idx보다 1큰 것이기 떄문
            #standard-1이 기준점이 되는 것이다.

            #돌이 1일때랑 0일때를 구분할 것
            #돌이 1일때, 그리고 서로가 같을 떄, 그리고 범위를 초과하지 않을때
            #idx를 확인해야하는데 값을 확인함

            #지금 오류 발생 원인을 찾았는데 왼쪽은 괜찮으나 오른쪽 범위를 벗어나게 되면 문제가 발생되는 것으로 확인됨
            #배열 크기가 N인데 N을 초과하지 않으면 실행이 되게 구현을 했고, 델타에서도 문제가 없었는데 왜 오류가 터지는 것..?

            if standard + i >= N: #델타값이 먹히지 않아서 일단 혹시 몰라서 적용을 했음
                break

            if arr[standard-i] == arr[standard+i] and arr[standard-i] == 1 and arr[standard+i] == 1 and 0 <= standard-i < N and 0 <= standard+i < N:
                arr[standard-i] = 0
                arr[standard+i] = 0
            #아닐떄를 바로  else로 두어도 되지만 범위 초과의 이슈가 발생하기 때문에 그대로 사용해준다.
            elif arr[standard-i] == arr[standard+i] and arr[standard-i] == 0 and arr[standard+i] == 0 and 0 <= standard-i < N and 0 <= standard+i < N:
                arr[standard-i] = 1
                arr[standard+i] = 1
    print(f'#{tc}', end = " ")
    print(*arr)