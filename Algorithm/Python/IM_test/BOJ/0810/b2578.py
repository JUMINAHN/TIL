#일단 빙고판 부터 채우자
bingo_pan = [list(map(int, input().split())) for _ in range(5)]
#그리고 나머지 input값 5개는 사회자가 부르는 번호 -> 내가 색칠할 것 나는 색칠할 경우 arr[row][col] = 0 할 것
#색칠을 하기위해선 루프를 모두 순회하고 if arr[row][col] == input값일 경우 --> arr[row][col] = input값
talk_number = [list(map(int, input().split())) for _ in range(5)]
talk = []
#print(talk_number)
for t in talk_number:
    talk.extend(t)
#print(talk)

def check_row(bingo_pan):
    bingo = 0
    for row in range(5):
        total = 0
        for col in range(5):
            if bingo_pan[row][col] == 0:
                total += 1
        if total == 5:
            bingo += 1
    return bingo

def check_col(bingo_pan):
    bingo = 0
    for col in range(5):
        total = 0
        for row in range(5):
            if bingo_pan[row][col] == 0:
                total += 1
        if total == 5:
            bingo += 1
    return bingo


def check_cross1(bingo_pan):
    bingo = 0
    for row in range(5):
        total = 0
        if bingo_pan[row][row] == 0:
            total += 1
        if total == 5:
            bingo +=1
    return bingo


def check_cross2(bingo_pan):
    bingo = 0
    for row in range(5):
        total = 0
        if bingo_pan[row][5-1-row] == 0:
            total += 1
        if total == 5:
            bingo += 1
    return bingo


for idx in range(len(talk)):
    for row in range(5): #빙고판에서
        for col in range(5):
            if bingo_pan[row][col] == talk[idx]: #내가 찾는 숫자라면
                bingo_pan[row][col] = 0 #0을 넣겠어요요

                bingo = check_col(bingo_pan)
                bingo += check_col(bingo_pan)
                bingo += check_cross1(bingo_pan)
                bingo += check_cross2(bingo_pan)
                if bingo == 3:
                    print(idx + 1)
                    break
    #채워진 빙고판 찾고 빙고 카운트하기
    #열 모두 돌았을 때 모두 0이라면 bingo 올리고, 행모두 돌렸을 떄 모두 0이라면 bingo 올리고, i==r이 모두 0이면 bingo
    #그렇다면 즉 그 요소들을 다 더해도 0이면 다 0이라는 소리잖아 -> 그걸 이용한다.
    #빙고를 카운트했을떄

