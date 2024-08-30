# 15분아까 사용함 9:12~10:19, 11:02
'''
1
2
##.
#.#

1
2
##.
#.#

1
4
#...
##..
....
#...
---->>> 해당 테스트케이스에서 오류
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input().strip()) #배열의 크기
    arr = [list(input()) for _ in range(N)] #arr에 데이터가 들어간다.

    first_row = first_col = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col] == '#':
                first_row = row
                first_col = col
                break #col loop를 빠짐
        if arr[first_row][first_col] == '#': #그러면 지금 들어간 상태이니까 내가 원하는게 나왔다면 break
            break

    second_col = 0
    for i in range(first_col, N):##이 있었던 곳 이후에 (이후면 일단 플러스 일을 해야하는데..)
        if arr[first_row][i] == '#':
            second_col = i #맨 마지막의 값이 담길 것
        else :
            break #없으면 그냥 끝내..?

    distance = second_col - first_col
    result = 'yes'
    for row in range(first_row, first_row+distance+1):
        # if row >= N:  # 배열 범위를 벗어나는 경우 체크 --> 근데 배열 범위를 벗어나면 애초에 idx error????
        #     result = 'no'
        #     break
        for col in range(first_col, first_col+distance+1):
            if arr[row][col] != '#':
                result = 'no'
                break
        if result == 'no':
            break

    if result == 'yes':#yes일떄 점검
        for row in range(N):
            for col in range(N): #그 범위 외에 해당 된다면
                if (row < first_row or row > first_row + distance or
                        col < first_col or col > first_col + distance):
                    if arr[row][col] == '#':
                        result = 'no'
                        break
            if result == 'no':
                break
    print(f'#{tc} {result}')
    #왜 no를 했을떄 enter을 쳐야할까?