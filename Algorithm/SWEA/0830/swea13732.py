#9:12~
import sys

sys.stdin = open('input13732.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #배열의 크기
    arr = [list(input()) for _ in range(N)] #arr에 데이터가 들어간다.

    first_row = first_col = 0
    # '#'이 있는 위치 탐색
    for row in range(N):
        for col in range(N):
            if arr[row][col] == '#': #가장 먼저 나오는 row위치 탐색
                #row / col에 값을 대입한다.
                first_row = row
                first_col = col
                break #여기서 빠져나가지 않아서 가장 끝에 있는게 찾아지게 됨
                #그리고 이 break는 col에 대한 break
        #큰 row에 대한 break는 어떻게 걸면 좋을까..?
        if arr[first_row][first_col] == '#': #그러면 지금 들어간 상태이니까 내가 원하는게 나왔다면 break
            break

    second_col = 0
    #그리고 그 row, 맨 뒤에서부터 접근을 하고, 그 위치를 찾는다.
    for i in range(N): #첫번째 행에서, 맨 마지막에 데이터 위치
        if arr[first_row][i] == '#':
            second_col = i #맨 마지막의 값이 담길 것
    # print(second_col) #원하는 값이 담겨 있음을 확인함

    distance = second_col - first_col #범위의 +1만큼 range를 돌면됨
    #print(distance) #맞게 들어감을 확인함
    result = 'yes'

    #첫번째 row를 기준으로
    for row in range(first_row, first_row+distance+1):
        # if '#' not in arr[row]:
        #     result = 'no'
        #     break
        for col in range(first_col, first_col+distance+1):
            if arr[row][col] != '#':
                #row = N #대입해도 고정 값이 있기 떄문에 안바뀔 것 같지만 일단 한다.
                result = 'no'
                break #이거는 col loop만 해당됨..
        if result == 'no': #no에서 빠져나갔다면 result가 no인 것
            break
    print(f'#{tc} {result}')
