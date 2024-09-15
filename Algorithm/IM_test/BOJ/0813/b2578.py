import sys
sys.stdin = open('input2578.txt')


bingopan = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]
#print(bingopan)
#print(call)

#call에 따라 색칠하기 --> visitied 위치에 개수가 5개이상이면 -> count1 증가 시킴
visited = [[0] * 9 for _ in range(4)] #4개 만들어야 함
#print(visited)

for c in call:
    for row in range(5):
        for col in range(5):
            #print(c, row, col)
            if c == bingopan[row][col]:
                visited[0][col] += 1
                visited[1][row] += 1
                visited[2][col-row] += 1
                visited[3][col+row] += 1

print(visited)