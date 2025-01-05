import sys

sys.stdin = open('input4861.txt')
#행마다 받아오기
def find_row(arr, N, M):
    if M % 2 == 0:
        for i in range(N):
            turn = arr[i][M//2:]
            #이걸 reverse해서 다시 담기
            turn = turn[::-1]
            #print(turn)
            #print(arr[i][:M//2])
            if arr[i][:M//2] == turn: #조건문 선정 값의 오류
                print(f'#{tc} {"".join(map(str, arr[i]))}') #같을 경우 행 자체를 출력한다.
    else :
        for i in range(N):
            turn = arr[i][M//2+1:]
            #이걸 reverse해서 다시 담기
            turn = turn[::-1]
            if arr[i][:M//2+2] == turn:
                print(f'#{tc} {"".join(map(str, arr[i]))}')  #같을 경우 행 자체를 출력한다.

#열마다 받아오기, 어떻게 하면 좋을까..
#배열에 담지않고
def find_col(arr, N, M):
    if M % 2 == 0:
        for i in range(N):
            turn = arr[M//2:][i]
            #이걸 reverse해서 다시 담기
            turn = turn[::-1]
            print(turn)
            #print(turn)
            #print(arr[i][:M//2])
            if arr[:M//2][i] == turn: #조건문 선정 값의 오류
                print(f'#{tc} {"".join(map(str, arr[i]))}') #같을 경우 행 자체를 출력한다.
    else :
        for i in range(N):
            turn = arr[M//2+1:][i]
            #이걸 reverse해서 다시 담기
            turn = turn[::-1]
            if arr[:M//2+2][i] == turn:
                print(f'#{tc} {"".join(map(str, arr[i]))}')  #같을 경우 행 자체를 출력한다.

#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #M은 찾고자 하는 길이
    arr = [list(input()) for _ in range(N)] #N*N의 배열
    find_row(arr, N, M)
    find_col(arr, N, M)



