import sys
sys.setrecursionlimit(10**7)

sys.stdin = open('input1217.txt')

#Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    t = int(input()) #그냥 이건 출력값
    N, M = map(int, input().split()) #9, 8일때 9를 8번 해야함

    # N ** M인데
    # 재귀함수 9 * 9 이걸 -> 8번
    #재귀 함수
    #무한 루프
    def zecop(M, N):
        if M == 0: #0번쨰 인덱스까지
            return 1
        else :
            M -= 1
            return N * zecop(M, N) #ecursionError: maximum recursion depth exceeded in compariso
    print(f'#{tc} {zecop(M, N)}')