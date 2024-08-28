#모르겠다..


import sys

sys.stdin = open('input4613.txt')

def up_and_down(N, M):
    #먼저 중요한 것은 맨위와 맨밑은 고정적인 값이 존재해야한다는 것
    #따라서 맨위가 white가 아닌 것 count
    #맨밑이 red가 아닌 것 count
    painting = 0
    for row in range(N):
        for col in range(M):
            if row == 0 and Russia[row][col] != 'W':
                painting += 1 #paint칠하는 것
            elif row == N-1 and Russia[row][col] != 'R': #red가 아니라면
                painting += 1
    #print(painting) #테스트 케이스 한번 맨위 맨 아래 보자
    #확인했을떄 의도에 맞게 확인되는 것을 볼 수 있음
    return painting

#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N은 행, M은 행
    Russia = [list(input()) for _ in range(N)] #러시아 국기 색칠 input
    top_down = up_and_down(N,M) #맨 위와 맨 아래 내역 확인
    #가운데를 순회하면서 어떤걸 채워넣으면 좋을지 판단하자 그러면 1번 idx부터 N-2번 idx까지 (range로는 N-1까지)

    #가운데를 찾습니다.
    #행별로 개수를 카운트한 것을 담는다.
    col_color_count = [] #red, blue, white에서 red를 없애
    for row in range(N-2,0,-1): #1번 idx부터 N-2번 idx까지 찾을 것이니까.
        w = b = r = 0
        for col in range(M):
            if Russia[row][col] == 'W':
                w += 1
            elif Russia[row][col] == 'B':
                b += 1
            else :
                r += 1
        col_color_count.append((w,b,r))
        #w,b,r 의 순서대로 가운데 행이 반복되고 있음
    print(col_color_count)
    #자 일단 해당 케이스가 될리는 없겠지만, 1번에서 가장 많은 행
    #복잡해진다..
    for a,b,c in col_color_count: #첫번쨰
        color = max(a,b,c) #가장 큰 color
        if color == 'W':
            pass

    #자 여기서 가장 큰 것의 기준으로
    #예를 들면 white누적합보다 blue누적합이 커지면 blue가되고 red 누적합이 커지면 red가 되는 행별로 count
    #blue칸에 갔는데 갑자기 white칸이 커진다고 해서 blue칸으로 갈 수 없음
    #최적화, 탐욕,, 그럼 뒤에서 접근

    #print(top_down)
    #5, 14



#아니면 극단적인 방법으로 white를 N-2까지 blue를 N-1까지 red를 N만
#모든 경우를 판단,, => 경우의 수 : 복잡해질 것 같음 (부분집합)