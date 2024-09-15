import sys

sys.stdin = open('input4835.txt')
#테스트 케이스 개수
T = int(input()) #Testcase -> 3개 들어옴
for tc in range(1, T+1):
    #정수의 개수, 구간의 개수  --> 총 정수 N, 구간의 개수 M
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    max_num = sum(ai[:M]) #가장 큰 것
    min_num = sum(ai[:M]) #가장 작은 것 #첫번째를 기준으로

    source = sum(ai[:M]) #비교할 비교 군위들
    for i in range(M, N): #idx 기준 -> M:3이면 -> M 이후부터 0 1 2 3 4  // M --> index 설정이 문제였다..\!!
        source = source + ai[i] - ai[i-M]
        if max_num < source:
            max_num = source
        elif min_num > source :
            min_num = source
    result = max_num - min_num
    print(f'#{tc} {result}')