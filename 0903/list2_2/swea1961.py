import sys
sys.stdin = open('input1961.txt')

def change90(N,arr):
    #새로운 배열
    new_arr = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            new_arr[row][col] = arr[N-1-col][row]
    return new_arr #90도 회전한 것

#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)] #배열안에 값을 넣기
    #받은 배열에 대해 회전
    arr90 = change90(N,arr) #90도 회전함
    arr180 = change90(N, arr90)
    arr270 = change90(N, arr180)
    make = list(zip(arr90, arr180, arr270))
    #print(make)
    print(f'#{tc}')
    for a,b,c in make:
        print("".join(map(str, a)), "".join(map(str, b)), "".join(map(str, c)))