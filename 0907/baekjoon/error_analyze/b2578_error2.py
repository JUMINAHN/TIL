import sys


def check_row(binggo):
    # 일단 행
    total = 0
    for row in range(N):
        if sum(binggo[row]) == 0:  # 빙고 한줄이 0이라면
            total += 1
    total2 = 0
    bing2 = list(map(list, zip(*binggo)))  # 전치 행렬
    for row in range(N):
        if sum(bing2[row]) == 0:
            total2 += 1
    return total + total2


def cross1(binggo):
    total = 0
    for i in range(N):
        total += binggo[i][i]
    if total == 0:
        return 1  # 한줄 찾았어요
    return 0  # 못찾았어요


def cross2(binggo):
    total = 0
    for i in range(N):
        total += binggo[i][N - 1 - i]
    if total == 0:
        return 1  # 한줄 찾았어요
    return 0  # 못찾았어요


sys.stdin = open('input2578.txt')
# N*N이니까 N을 만들어주자
N = 5
K = 3  # 찾을 개수
# 빙고판 input
binggo = [list(map(int, input().split())) for _ in range(N)]
# 사회자번호 input
talk = [list(map(int, input().split())) for _ in range(N)]
# 우리가 얻고 싶은것은 사회자가 몇번째 부를때 빙고를 외치는가? -> 1부터 25까지 부른다.. ***주의할 것 1로 시작한다.
# 단순하게 1차원 배열로 몇번쨰인지 얻고 싶어서
talk_num = []  # talk_num에 input받은 talk를 넣을 것
for row in range(N):
    for col in range(N):
        talk_num.append(talk[row][col])  # 순서대로 append
# print(talk_num)

# 빙고 순서 -> 루틴
# 1.사회자가 순서를 부른다. -> 즉 for문을 돌거나 while문을 돌면서 idx를 말한다.
# 여러개의 for문이 헷갈리면 while을 쓴다.
# 먼저 사회자가 순서를 부르면 -> 빙고판에서 찾아야한다 -> 즉 bingopan을 모두 돌아야 사회자가 부른것을 확인할 수 있다.
idx = 0  # 0부터 시작하니까. -> 0은 1과 같다
Flag = True
while Flag:  # 24까지니까
    if idx >= (N * N - 1):
        break
    # print(idx)
    # 2. 사회자가 부른 순서를 빙고판에서 색칠을 하고 -> 일단 행으로만 순회해도 됨
    for row in range(N):
        for col in range(N):
            if binggo[row][col] == talk_num[idx]:  # 같다면 -> 오타
                binggo[row][col] = 0  # 0으로 색칠을 한다.

                # 색칠했을 때-> 색칠한 빙고판으로 보기 떄문에 if문 안에서 실행해줘야 할듯 -> 한 줄 한 줄 마다 점검? -> 모두 순회하고 최종?**** 고려하기
                row_col_sum = check_row(binggo)  # 행 -> 열 모두
                leftright = cross1(binggo)
                rightleft = cross2(binggo)
                # 3. 색칠한 빙고판을 보고, 3줄인지 계속확인해주기
                # 색칠한 빙고판을 보려면 행, 열, 오->왼 대각선, 왼 -> 오 대각선을 모두 검토 해야한다.
                if row_col_sum + leftright + rightleft >= K:  # 3 이상일 때
                    # print(idx)
                    Flag = False
                    # idx = N*N*N #while문 자체를 종료시키기 위함 -> 이거 떄문에
                    break  # for col문 break
        if Flag == False:
            break  # 빠져나가
    if Flag == False:
        break  # 빠져나가
    idx += 1  # 그리고 다음ㅇ 순서를 찾을 수 있또록 idx를 카운트한다.

print(idx+1)  # 부른게 0이니까

'''
#빙고판 input
#사회자번호 input
#우리가 얻고 싶은것은 사회자가 몇번째 부를때 빙고를 외치는가? -> 1부터 25까지 부른다.. ***주의할 것 1로 시작한다.

#빙고 순서 -> 루틴
#1.사회자가 순서를 부르고
#2. 사회자가 부른 순서를 빙고판에서 색칠을 하고
#3. 색칠한 빙고판을 보고, 3줄인지 계속확인해주기 
'''