import sys

sys.stdin = open('input1961.txt')

def change_direct(arr, N):
    new_arr = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            new_arr[row][col] = arr[N-1-col][row]
    return new_arr

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #그만큼 N*N모양의 크기를 만들 것
    arr = [list(map(int, input().split())) for _ in range(N)] #arr데이터

    arr1 = change_direct(arr, N)
    arr2 = change_direct(arr1, N)
    arr3 = change_direct(arr2, N)
    #해당 for문 잘 알아두기
    print(f'#{tc}')
    for a, b, c in list(zip(arr1, arr2, arr3)): #data에 d하면 한줄씩 나오는 것과 유사함
        #join 메서드 정말 잘 활용하기 -> list를 예쁘게 묶어주는 애들
        print(f'{"".join(map(str, a))} {"".join(map(str, b))} {"".join(map(str, c))}')


