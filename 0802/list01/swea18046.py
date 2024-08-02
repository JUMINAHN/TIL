import sys

sys.stdin = open('input18046.txt')

T = int(input()) #testcase 3 입력
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    max_num = num_list[0]
    min_num = num_list[0]
    #가장 큰 수와 가장 작은 수
    for i in range(N): #0부터 1까지 # 버블정렬 사용해도 됨
        if min_num > num_list[i]:
            min_num = num_list[i]
        if max_num < num_list[i]:
            max_num = num_list[i]
    print(f'#{tc} {max_num - min_num}')