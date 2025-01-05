import sys

sys.stdin = open('input20397.txt')

# Testcase 수
T = int(input()) #Testcase만큼
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        standard, R = map(int, input().split())
        standard = standard - 1
        for i in range(1, R+1):

            if  0 <= standard-i < N and 0 <= standard+i < N and arr[standard-i] == arr[standard+i] and arr[standard-i] == 1: #왜 안돼? #4 4
                arr[standard-i] = 0
                arr[standard+i] = 0
            elif 0 <= standard-i < N and 0 <= standard+i < N and arr[standard-i] == arr[standard+i] and arr[standard-i] == 0 :
                arr[standard-i] = 1
                arr[standard+i] = 1
    print(f'#{tc}', end = " ")
    print(*arr)