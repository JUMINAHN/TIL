import sys

sys.stdin = open('input5789.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split()) #1부터 N까지에 있는 것, Q는 반복할 횟수
    arr = [0] * N #N개 만큼은 맞으니까 (1번부터 5까지라고 해도 -> 총 5개는 맞으니까)
    for i in range(1, Q+1):
        L, R = map(int, input().split()) #1번 idx부터 3번 idx까지 -> 0번부터 2번까지 .. 즉 range3까지
        for j in range(L-1, R): #0번 idx
            arr[j] = i
    print(f'#{tc}', end = " ")
    print(*arr)