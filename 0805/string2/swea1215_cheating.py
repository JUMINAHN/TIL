import sys

sys.stdin = open('input1215.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    matrix = [input() for _ in range(8)]

    cnt = 0
    # 행마다 회문 검색
    for i in range(8):
        # N 개의 문자열로 된 회문이 있는지 검색
        for j in range(8 - N + 1):
            # 각 위치에서 회문 검사
            for k in range(N // 2):
                if matrix[i][j + k] != matrix[i][j + N - k - 1]:
                    break
            else: #for루프가 정상적으로 모든 반복을 완료했을 떄 else 블록이 실행됨
                cnt += 1

    # 열마다 회문 검색
    for j in range(8):
        # N 개의 문자열로 된 회문이 있는지 검색
        for i in range(8 - N + 1):
            # 각 위치에서 회문 검사
            for k in range(N):
                if matrix[i + k][j] != matrix[i + N - k - 1][j]:
                    break
            else:
                cnt += 1

    print(f'#{tc} {cnt}')