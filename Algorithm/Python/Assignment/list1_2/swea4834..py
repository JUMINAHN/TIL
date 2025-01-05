# import sys
#
# sys.stdin = open('input4834.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = [0] * 10 #9개의 숫자 카드를 셀거기 떄문에
    arr = list(map(int, input()))
    for a in arr:
        count[a] += 1

    max_idx = 0
    max_num = 0
    for i in range(len(count)):
        if count[max_idx] <= count[i]: #카드 장수가 같을 떄 적힌 숫자가 큰 쪽
            max_idx = i
            max_num = count[i] #배열을 기반으로 count한 것들
    print(f'#{tc} {max_idx} {max_num}')
