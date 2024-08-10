S = 100
arr = [[0] * S for _ in range(S)] #100 * 100크기 만들어짐

N = int(input()) #색종이 개수
for _ in range(N):
    col, row = map(int, input().split())

    for i in range(S-1-row, S-1-(row+10), -1): #뺴는 것을 이상하게 함 -> 헷갈리면 직접 손으로 작은 단위는 계산해보자
        for j in range(col, col+10):
            if arr[i][j] == 1:
                continue
            arr[i][j] = 1

total = 0
for row in range(S):
    for col in range(S):
        if arr[row][col] == 1:
            total += 1
print(total)