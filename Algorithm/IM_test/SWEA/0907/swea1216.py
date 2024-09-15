import sys

sys.stdin = open('input1216.txt')
#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    N = 100 #size 100*100자리 회문
    #A한개짜리도 회문임
    #가로/세로 모두 판단
    test_case = int(input())
    arr = [list(input()) for _ in range(N)]
    #print(arr)

    #회문
    #가장 길이가 긴 회문
    max_len = 0
    #행
    for row in range(N):
        for i in range(0,N):
            for j in range(i, N): #
                data = []
                for col in range(i, j+1): #0,0까지
                    data.append(arr[row][col])
                if data == data[::-1]:
                    #print(data)
                    if max_len < len(data):
                        max_len = len(data)
    #전치행렬
    arr2 = list(map(list, zip(*arr)))
    for row in range(N):
        for i in range(0,N):
            for j in range(i, N): #
                data = []
                for col in range(i, j+1): #0,0까지
                    data.append(arr2[row][col])
                if data == data[::-1]:
                    #print(data)
                    if max_len < len(data):
                        max_len = len(data)
    print(f'#{test_case} {max_len}')

