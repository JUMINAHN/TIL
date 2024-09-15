import sys
#이거 진짜 다시해야 해


sys.stdin = open('input2001.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #파리 퇴치
    N, M = map(int,input().split())
    pari = [list(map(int, input().split())) for _ in range(N)] #파리 개체 수 담기

    max_pari = 0 #초기값 0설정

    for j in range(0, N-M+1):
        for i in range(0, N-M+1): #오탈
            sum_pari = 0
            for row in range(j, M+j):
                for col in range(i, M+i):
                    sum_pari += pari[row][col] #list index out of range
            if max_pari < sum_pari:
                max_pari = sum_pari

    print(f'#{tc} {max_pari}')


    # for i in range(0, N-M+1):
    #     for row in range(i, M+i):
    #         for j in range(0, N-M+1):
    #             sum_pari = 0
    #             for col in range(j, M+j):
    #                 sum_pari += pari[row][col]
    #             if max_pari < sum_pari:
    #                 max_pari = sum_pari


    # for row in range(0, N-M+1) : #모든 행 순회 -> 단 간격의 행은 범위초과 가능성으로 돌지 않음
    #     for i in range(0,N-M+1) : #동일하게 작용할 것 -> 원하는 범위 값 -> 1이 되면
    #         sum_pari = 0
    #         for col in range(i, i+M): #해당 for문은 2*2만큼만 돌기 위함 -> 예를 들면 0~2 -> 1부터 3까지
    #             sum_pari += pari[row][col]
    #         if max_pari < sum_pari:
    #             max_pari = sum_pari
