# import sys
#
# sys.stdin = open('input1954.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_num = min(arr)
    max_num = max(arr)
    #print(min_num)
    #print(max_num)
    print(f'#{tc} {max_num - min_num}')