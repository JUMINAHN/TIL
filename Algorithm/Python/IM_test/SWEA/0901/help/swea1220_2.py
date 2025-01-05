#문어박사
import sys

sys.stdin = open('input1220.txt')
#테스트 케이스 개수
T = 10  # 테스트 케이스의 수
for test_case in range(1, T + 1):  # 각 테스트 케이스에 대해 반복
    N = int(input())  # N x N 배열의 크기 입력
    # N x N 크기의 2차원 배열 입력 받기
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0  # 교착 상태 카운트 초기화
    # 열 우선 순회
    for col in range(N):  # 각 열에 대해
        prev = 0  # 이전 값 초기화 (0: 빈 칸, 1: N극, 2: S극)
        for row in range(N):  # 각 행에 대해 (위에서 아래로)
            n = arr[row][col]  # 현재 위치의 값
            #print(n)
            if n:  # n이 0이 아닐 때 (자성체가 있을 때)
                # n이 1과 2일때
                #이 조건은 현재 값(n)이 S극(2)이고, 이전에 만난 값(prev)이 N극(1)일 때를 확인
                #n이 2일 때를 체크하는 이유는 S극이 위에 있고 N극이 아래에 있을 때만 교착 상태가 발생하기 때문 --> 이게 핵심 패턴
                #n이 1일 때를 체크하면 반대 상황(S극이 아래, N극이 위)을 찾게 되는데, 이는 문제의 조건에 맞음
                if n == 2 and prev == 1:  # 현재 S극(2)이고 이전이 N극(1)이면
                    ans += 1  # 교착 상태 카운트 증가
                prev = n  # 현재 값을 이전 값으로 저장
                #이 줄은 현재 값을 다음 반복을 위해 저장
                #매 반복마다 현재 값(n)이 다음 반복의 이전 값(prev)
    # 결과 출력
    print(f'#{test_case} {ans}')