import sys

sys.stdin = open('input1961.txt')

def first_turn(N, arr):
    #이부분을 순회해해야함
    #일단 row는 위로 콜럼은 원래방향
    result = []
    for col in range(N):
        for row in range(N-1, -1, -1):
            result.append(arr[row][col])
    return result

def second_turn(N, arr):
    result = []
    #2번쨰는 돌아간 상태에서 column역순 column이 돌아가는게 우선
    for row in range(N-1, -1, -1):
        for column in range(N-1, -1, -1):
            result.append(arr[row][column])
    return result

def third_turn(N,arr):
    result = []
    #row먼저 증가하고 맨 오른쪽 열부터 시작
    for column in range(N-1, -1, -1):
        for row in range(N):
            result.append(arr[row][column])
    return result

T = int(input()) #test1개
for tc in range(1, T+1):
    N = int(input()) #로우 행 개수 #input으로 받을 3
    arr = [list(map(int, input().split())) for _ in range(N)]

    first = first_turn(N,arr)
    second = second_turn(N,arr)
    third = third_turn(N,arr)
    final_list = first + second + third #3개니까 27개 -> 9개 들어있으니까
    print(final_list)
    #9TLr 짜르기
    print(final_list[0:3]+final_list[9:12]+final_list[18:21])



