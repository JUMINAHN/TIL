import sys

sys.stdin = open('input4835.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #for 구문으로 풀기
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    #구간만큼 순회하기.

    #min_num 자체를 0으로 고정했기 때문에 문제가 발생함
    min_num = 0
    max_num = 0

    #자 range 범위랑, 범위는 맞게 측정되었지만 "작은 값"을 구할 떄 문제가 발생
    #이 N-M이런거에 취약한듯
    for i in range(N-M+1): #그렇다면 N의 범위가 초과될 수 있기 때문에 N-M을 해줘야 한다.
        sum = 0
        for j in range(i, i+M): #원하는 범위만 큼 순회할 것 -> i 기준으로
            sum += ai[j]
        if i == 0: #그래서 0번째 인덱스의 결과값을 min과 max에 박고 시작한다.
            min_num = max_num = sum
        if max_num < sum :
            max_num = sum
        elif min_num > sum:
            min_num = sum
    #print(max_num)
    #print(min_num)
    result = max_num - min_num
    print(f'#{tc} {result}')
