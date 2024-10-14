# 길이가 M인 수열을 모두 구하는 프로그램
# 1부터 N까지 중복없이 M개를 고른 수열
#1부터 N까지 중복없이 M개를 고른 수열
#재귀 구조로?

#N개, M개?

"""
1. 참고
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(방문 여부 확인)
- 재귀함수에서 M개를 선택할경우 print

2. 시간 복잡도
- N! > 가능

3. 자료구조
- 결과값 저장 int[]
- 방문여부 체크 bool[]
"""

import sys
input = sys.stdin.readline  # 입력 속도 향상을 위해 sys.stdin.readline 사용

# N: 1부터 N까지의 자연수, M: 선택할 숫자의 개수
N, M = map(int, input().split())

result = []  # 현재 선택된 숫자들을 저장할 리스트
visited = [False] * (N + 1)  # 각 숫자의 사용 여부를 표시할 리스트 (0은 사용하지 않으므로 N+1 크기로 생성)


def recur(num):
    # num: 현재까지 선택한 숫자의 개수
    if num == M:  # M개의 숫자를 모두 선택했다면
        print(' '.join(map(str, result)))  # 현재 결과를 출력
        return

    for i in range(1, N + 1):  # 1부터 N까지의 숫자에 대해
        if not visited[i]:  # i번째 숫자를 아직 사용하지 않았다면
            visited[i] = True  # i번째 숫자를 사용했다고 표시 -> 방문 체크 후
            result.append(i)  # 결과 리스트에 i 추가 -> append

            recur(num + 1)  # 다음 숫자를 선택하기 위해 재귀 호출 == len처럼 동작함 == 쌓이는 효과
            #1이 선택되었으니까 그 다음에 -> 높이1 -> 높이 2

            visited[i] = False  # i번째 숫자 사용 표시를 취소 (백트래킹)
            result.pop()  # 결과 리스트에서 i 제거 (백트래킹)


recur(0)  # 0개의 숫자로 시작하여 재귀 함수 호출
"------------------------------------------------- : 이런 느낌이 아닌가요?"

# #N개, M개?
# def recursive(start, N, M):
#     if start >= N: #3일떄까지
#         return
#     for i in range(start):
#         for col in range(i+1, start):
#             print(i, col)
#     recursive(start+1, N, M)
#
# recursive(1, N, M)

