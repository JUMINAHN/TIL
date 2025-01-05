# T = int(input())
# for tc in range(1, T+1):
N, M = map(int, input().split())  # N: 스크린 크기, M: 바구니 크기
J = int(input())  # 사과의 개수
apples = [int(input()) for _ in range(J)]  # 사과가 떨어지는 위치들
print(apples)
move_count = 0  # 바구니 이동 횟수
left = 1  # 바구니의 왼쪽 끝 위치 (1부터 시작)

for apple in apples:
    # 바구니의 오른쪽 끝 위치
    right = left + M - 1

    # 사과가 바구니의 왼쪽에 떨어지는 경우
    while apple < left:
        left -= 1
        move_count += 1

    # 사과가 바구니의 오른쪽에 떨어지는 경우
    while apple > right:
        left += 1
        right += 1
        move_count += 1

print(move_count)