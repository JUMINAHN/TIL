#import sys

#sys.stdin = open('input4835.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N개의 정수가 들어있는 배열 M개의 합을 계산해야 함
    arr = list(map(int, input().split()))
    #3개씩 -> 1 2 3
    data_list = arr[0:M]#M개만큼
    data_sum = sum(data_list)
    #print(data_sum)
    max_sum = sum(data_list)
    min_sum = sum(data_list)
    for i in range(M,N):
        data_sum = data_sum - arr[i-M] + arr[i]
        #print(data_sum)
        if max_sum < data_sum:
            max_sum = data_sum
        elif min_sum > data_sum:
            min_sum = data_sum
    #문제를 잘 읽자
    print(f'#{tc} {max_sum - min_sum}')
    #print(max_sum)
    #print(min_sum)