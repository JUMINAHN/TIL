import sys
from collections import deque

sys.stdin = open('input5105.txt')

T = int(input())
for tc in range(1, T + 1):
    def BFS(row, col):
        queue = deque()
        queue.append((row, col))
        visited = [[0] * N for _ in range(N)] #여기는 방문 배열을 사용함
        visited[row][col] = 1

        while queue:
            r, c = queue.popleft()
            for k in range(len(data_row)):
                move_r = r + data_row[k]
                move_c = c + data_col[k]
                if not (0 <= move_r < N and 0 <= move_c < N) or miro[move_r][move_c] == 1:
                    continue
                if miro[move_r][move_c] == 3:
                    return visited[r][c] - 1  # 시작점은 카운트하지 않으므로 1을 빼줍니다 -> #방문에 대한 것을 확인
                if miro[move_r][move_c] == 0 and visited[move_r][move_c] == 0:
                    visited[move_r][move_c] = visited[r][c] + 1 #방문값을 증가시키고 -> visited에 대한 내용을 추가한 것 뿐
                    queue.append((move_r, move_c))
        return 0


    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    data_row = [0, 0, 1, -1]
    data_col = [1, -1, 0, 0]

    start_row, start_col = 0, 0
    flag = True
    for row in range(N):
        for col in range(N):
            if miro[row][col] == 2:
                start_row, start_col = row, col
                flag = False
                break
        if flag == False:
            break

    result = BFS(start_row, start_col)
    print(f'#{tc} {result}')