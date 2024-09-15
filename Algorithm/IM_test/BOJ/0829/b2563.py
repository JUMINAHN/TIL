import sys
sys.stdin = open('input2563.txt')

W = 100  # 넓이를 구할것이기 떄문에 width를 상상하며 100을 선언
papper = [[0] * W for _ in range(W)]  # 색종이를 만든다.
N = int(input())  # 색종이 개수
for _ in range(N):  # 색종이 개수만큼 반복한다.
    C, R = map(int, input().split())  # 색종이 col, row를 확인하고, 색칠할 영역을 확보한다.
    K = 10  # 가로 세로가 10인 정사각형의 검은색 종이를 나타냄
    for row in range(N - R, N - R - K, -1):  # row는 위로 올라가야하기 떄문에
        for col in range(C, C + K):
            papper[row][col] = 1

total = 0
for row in range(W):
    for col in range(W):
        if papper[row][col] == 1:
            total += 1
print(total)