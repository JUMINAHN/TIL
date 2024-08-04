# 1. 일단 칸을 [0] * 11 리스트컴프리핸션을 돌려야 한다. -> 0부터 10칸 까지기 떄문에
# 2. r1 c1 r2 c2 RGB -> RGB일 경우 헨젤과 그레텔 arr[row][col] = RGB
# 3. r1c1의 부분을 색칠하기 떄문에 영역 자체임을 확인하고 색칠한다
# 4. 칠해지는 개수가 계속 바뀌기 떄문에 N개로 받은 만큼 그 해당 되는 값을 매개변수로 담는게 편할 것 같다.

import sys

sys.stdin = open('input18059.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [([0]*11) for _ in range(11)]
    #r1, c1, r2, c2, RGB = map(int, input().split()) #여러개 들어올 때
    box_info = [list(map(int, input().split())) for _ in range(N)] #행의 개수

    for b_i in box_info: #b_i의 [0]번째 [2번째], [1]번째  [3번째], [4번째]
        for row in range(b_i[0], b_i[2]+1): #범위 설정을 잘못했었나보다 -> 3칸이 들어가려면 이렇게 지정하는게 맞음
            for col in range(b_i[1], b_i[3]+1):
                if arr[row][col] != 0:
                    arr[row][col] += b_i[4]
                else :
                    arr[row][col] = b_i[4] #RGB에 값 대입

    #전체 순회
    total = 0
    for row in range(11):
        for col in range(11):
            if arr[row][col] == 3:
                total += 1

    print(f'#{tc} {total}')

# for row in range(r1, r2 + 2):
#     for col in range(c1, c1 + 2):
#         arr[row][col] += RGB