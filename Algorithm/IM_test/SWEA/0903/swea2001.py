#import sys
#sys.stdin = open('input2001.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    #testcase 2개만 맞음
    N, M = map(int, input().split())
    pari = [list(map(int, input().split())) for _ in range(N)] #파리 배치
 #c천천히 접근
    max_total = 0
    for j in range(0, N-M+1):
        for i in range(0, N-M+1):
            total_sum = 0
            for row in range(j, M+j):
                for col in range(i,M+i):
                    total_sum += pari[row][col]
            if max_total < total_sum:
                max_total = total_sum
    print(f'#{tc} {max_total}')