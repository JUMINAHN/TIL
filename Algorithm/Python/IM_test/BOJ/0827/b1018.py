N, M = map(int, input().split())
K = 8
arr = [list(input().strip()) for _ in range(N)] #체스판을 만들고

# arr범위를 돌면서 8*8배열을 확인한다.
total_min = []

for row in range(N-K+1):
    for col in range(M-K+1):
        #첫번째 8*8을 돌 때 내용 카운트
        w_count = 0
        b_count = 0
        for i in range(row, row+K):
            for j in range(col, col+K):
                if (i+j) % 2 == 0 : #chess모양 (0,0) (1,1)이 같은 것 그런 케이스 고려
                    if arr[i][j] != 'W' :# 0이면
                        w_count += 1 #아니면 카운트
                    if arr[i][j] != 'B': #else로 안하고 그냥 if로 하는 이유
                        b_count += 1
                else : # 그 반대라면
                    if arr[i][j] != 'B':
                        w_count += 1
                    if arr[i][j] != 'W':
                        b_count += 1
        total_min.append(w_count)
        total_min.append(b_count)
print(min(total_min))