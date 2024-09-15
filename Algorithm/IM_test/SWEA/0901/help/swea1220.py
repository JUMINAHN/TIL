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
    # 전치행렬 만들기 (열을 행으로 변환)
    arr_t = list(zip(*arr))
    # 전치된 배열의 각 행(원래 배열의 각 열)에 대해 처리
    for lst in arr_t:
        prev = 0  # 이전 값 초기화 (0: 빈 칸, 1: N극, 2: S극)
        # 현재 행(원래 열)의 각 원소에 대해 처리
        for n in lst:
            if n:  # n이 0이 아닐 때 (자성체가 있을 때)
                if n == 2 and prev == 1:  # 현재 S극(2)이고 이전이 N극(1)이면
                    ans += 1  # 교착 상태 카운트 증가
                prev = n  # 현재 값을 이전 값으로 저장
    # 결과 출력
    print(f'#{test_case} {ans}')