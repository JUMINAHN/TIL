#문어박사 풀이..
N = 5
bingo = [list(map(int, input().split())) for _ in range(N)] #빙고판에 값 다 넣었음
facilitator = [] #사회자가 부를 번호 (idx는 24까지)_값을 구하기 위해선 i+1을 해줘야 함
for _ in range(N):
    for i in list(map(int, input().split())):
        facilitator.append(i)

#빙고판에 count를 해줘야함 색칠을 해주기 위해서 나는 새로운 빙고판을 만들겠음
#check_bingo = [[0]*N for _ in range(N)] #빙고판 25개 만들고
#facilitator의 1번째와 bingopan에 내용이 같다면, 색칠을 한다.
visited = [[0]*10 for _ in range(N)] #visited[4]개를 해야함

idx = 0
total = 0
for row in range(N):
    for col in range(N):
        if facilitator[idx] == bingo[row][col]:
            visited[0][row] += 1 #visited 0번째 배열에 idx 접근
            visited[1][col] += 1
            visited[2][row+col] += 1
            visited[3][row-col] += 1

        for v in visited:
            if v == 5:
                total += 1
        idx += 1

        if total >= 3:
            row = N+1 #row가 끝나게 만들어버리고
            break
print(idx)


        #count가 되었다 여기서 visited[0]에 한줄이라도 5이상이면 +1

