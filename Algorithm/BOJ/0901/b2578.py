# import sys
#
# sys.stdin = open('input2578.txt')

def check_row(N, binggo):
    #행 우선 점검
    total = 0
    for row in range(N):
        #첫번쨰 row의 합산
        row_total = 0
        for col in range(N):
            row_total += binggo[row][col]
        if row_total == 0:
            total += 1
    return total

def check_col(N, binggo):
    #열 우선 점검
    total = 0
    for col in range(N):
        #첫번쨰 row의 합산
        col_total = 0
        for row in range(N):
            col_total += binggo[row][col]
        if col_total == 0:
            total += 1
    return total

def cross_1(N, binggo): #왼 ->오
    sum_total = 0
    total = 0
    for i in range(N):
        sum_total += binggo[i][i]
    if sum_total == total:
        total += 1
        return total
    return 0 #아닐 경우 일단 0반환

def cross_2(N, binggo):
    sum_total = 0
    total = 0
    for i in range(N):
        sum_total += binggo[i][N-1-i]
    if sum_total == total:
        total += 1 #토탈을 증가시키지 않은 문제.. 왜이렇게 실수를 하는가
        return total
    return 0 #아닐 경우 일단 0반환

#테스트 케이스 개수
# T = int(input())
# for tc in range(1, T+1):
N = 5
K = 3
binggo = [list(map(int, input().split())) for _ in range(N)] #빙고의 범위
#사회자가 말하는 것
facilitator = [list(map(int, input().split())) for _ in range(N)] #이거 자체를 배열 없이 만들고 싶음
announce = [] #facilitator의 idx만큼 수정하기 -> print를 할땐 해당 idx + 1을 해야 1부터 선언한 수가 됨
for row in range(N):
    for col in range(N):
        announce.append(facilitator[row][col])
#print(len(announce))
#부르고 색칠을 하고 점검
talk_idx = 0
result_idx = 0
#    print(announce[24])

while talk_idx <= (N*N)-1 :
    color_row = 0
    color_col = 0
    for row in range(N): #0부터 5까지
        for col in range(N): #0부터 5까지 #11을 삭제..?
            if binggo[row][col] == announce[talk_idx]: #이게 왜 범위 초과 ? -< anounce떄문인데 -> 25를 넘기는 문제가 발생해서
                color_row = row
                color_col = col #색칠할 것들을 넣어줘
                #break# col break
    #10을 삭제해야하는데 11을 삭제하고 있다..?
    binggo[color_row][color_col] = 0 #해당 되는 사회자가 부른 곳에 0을 색칠 하고 -> 여기 값이 안바뀐다. -> 잘못넣음 ㅡㅡ
    if talk_idx >= 5:  # 한줄이 완성된다고 가정했을떄부터 점검을 하면 됨
        result = check_row(N, binggo) + check_col(N, binggo) + cross_1(N, binggo) + cross_2(N, binggo)
        #print(result) #합산이 제대로 안되는 것을 볼 수 있음 -> 맞음
        if result >= K:  # K가 3이상이면
            #print(talk_idx)
            result_idx = (talk_idx +1)
            #talk_idx = N*N + 5
            break
    talk_idx += 1 #talk_idx는 증가시켜줌

print(result_idx)
#

