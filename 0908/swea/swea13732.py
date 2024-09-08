import sys

sys.stdin = open('input13732.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #먼저 범위 탐색을 위해서 첫번쨰 #이 있는 위치, 그리고 그 행에 마지막으로 #이 등장하는 위치를 구한다.
    sqaure = [list(input()) for _ in range(N)]

    r1 = c1 = 0
    find = 0 #찾았음을 확인하기 위해서
    for row in range(N): #어짜피 여기서 벗어 나지 못함 break를 걸어도 col에서만 벗어남
        for col in range(N):
            if sqaure[row][col] == '#':
                r1 = row
                c1 = col
                find += 1
                break #col이 break
        if find > 0:
            break
    #print(r1,c1)
    find1 = 0
    r2 = c2 = 0
    for row in range(N-1, -1, -1):
        for col in range(N-1, -1, -1):
            if sqaure[row][col] =='#':
                r2= row
                c2 = col
                find1 += 1
                break
        if find1 > 0:
            break
    if r2 - r1 == c2 - c1:
        result = 'yes'
        #이제 원하는 범위 => 정사각형 내부 검토
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                if sqaure[row][col] == '.':
                    result = 'no'
                    break #col을 나간다.
            if result == 'no': #0보다크니까 1을 찾은 것
                break #더 볼 필요도 없이 그니까 NO니까
        #내부에서 검토하니까 문제가 되는 것

        #이제 외부 -> 문제가 있는 것들은 틀린거니까 검토할 필요가 없음 -> 이제 없는 것들을 위주로 검토
        #if result == 'yes': #yes면 한 번 더 검토
            #아까 내부 범위를 일단 다 .으로 만들고 #가 있는지 확인만
        for row in range(r1, r2 + 1):
            for col in range(c1, c2 + 1):
                if sqaure[row][col] == '#':
                    sqaure[row][col] = '.'
        #print(sqaure)
        #그리고 다시 전체 탐색
        for row in range(N):
            for col in range(N):
                if sqaure[row][col] == '#':
                    result = 'no'
                    break
            if result == 'no':
                break
    else:
        result = 'no'

    print(f'#{tc} {result}')

