import sys

sys.stdin = open('input2805.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #농작물의 크기
    seed = [list(map(int, input())) for _ in range(N)]

    layer = N//2
    #print(layer)
    total = 0
    #일단 반으로 잘라서 생각할 것
    for row in range(N//2+1):
        for col in range(layer-row, layer+row+1):
            total += seed[row][col]
    #print(total)
    #그리고 그 절반
    reverse_seed = seed[::-1] #동일하게 접근
    for row in range(N//2): #가운데는 계산했으니 할필요가 없음
        for col in range(layer-row, layer+row+1):
            total += reverse_seed[row][col]
    print(f'#{tc} {total}')