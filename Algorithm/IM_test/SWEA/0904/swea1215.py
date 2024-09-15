#import sys

#sys.stdin = open('input1215.txt')
# input값의 오류로 값이 뜨지 않았음
# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = 8
    K = int(input()) #찾아야하는 길이
    arr = [input() for _ in range(N)]
    #print(arr)
    #전체를 모두 점검해야하는 문제
    #행탐색, 열탐색 진행을 해야 함

    total = 0 #회문을 카운트할 변수
    #2. row는 모두 탐색해야함
    for row in range(0, N):
    #1-1. 그리고 다음 열을 탐색하기 위해서 1부터 K+1만큼 게산 필요
        #이는 즉 i부터 k+i만큼 필요함
        for i in range(0, N-K+1):
    #1. 일단 행을 탐색할 경우 일부열에 대한 점검이 필요 -> 0부터 k만큼
            data = []
            for col in range(i, K+i):
                data.append(arr[row][col])
            if data == data[::-1]:
                total += 1
    #동일하게 col진행
    #total = 0  # 회문을 카운트할 변수
    # 2. row는 모두 탐색해야함
    for col in range(0, N):
        # 1-1. 그리고 다음 열을 탐색하기 위해서 1부터 K+1만큼 게산 필요
        # 이는 즉 i부터 k+i만큼 필요함
        for i in range(0, N - K + 1):
            # 1. 일단 행을 탐색할 경우 일부열에 대한 점검이 필요 -> 0부터 k만큼
            data = []
            for row in range(i, K + i):
                data.append(arr[row][col])
            if data == data[::-1]:
                total += 1
    print(f'#{tc} {total}')
