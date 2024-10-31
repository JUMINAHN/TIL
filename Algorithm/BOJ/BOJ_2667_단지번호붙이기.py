import sys
sys.setrecursionlimit(10**6)

N = int(input()) #정사각형
apart = [list(input()) for _ in range(N)]


def dfs(row, col, apart_idx):
    apart[row][col] = apart_idx

    for i in range(4):
        move_row = row + data_row[i]
        move_col = col + data_col[i]
        if not (0 <= move_row < N and 0 <= move_col < N) or apart[move_row][move_col] == '0': #0일 경우
            continue #패스
        if apart[move_row][move_col] == -1: #-1이 될경우
            #방문 처리를 한다
            apart[move_row][move_col] = apart_idx #apart_idx로
            dfs(move_row, move_col, apart_idx) #idx는 증가해야 함 => 증가하지 않고 있는 문제 확인
    return

apart_complex = 0
apart_idx = 1

data_row = [0, 1, 0, -1]
data_col = [1, 0, -1, 0] #우 하 좌 상

for row in range(N):
    for col in range(N):
        if apart[row][col] == '1': #1은 문자열임
            apart[row][col] = -1 #-1값을 대입해준다 => 여기서 에러 발생
#모든 루프를 돌고

for row in range(N):
    for col in range(N): #1이면 count
        if apart[row][col] == -1: #apart가 1이면
            apart_complex += 1
            dfs(row, col, apart_idx) #dfs로 방문한다. => 단지 내 집의 수 =
            apart_idx += 1

print(apart_complex)
result = []
for i in range(1, apart_complex+1):
    inner_count = 0
    for row in range(N):
        for col in range(N):
            if apart[row][col] == i:
                inner_count += 1
    result.append(inner_count)
result.sort()
for r in result:
    print(r)

