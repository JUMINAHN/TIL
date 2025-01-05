import sys

sys.stdin = open('input9386.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #연속한 1의 개수 중 최대값을 출력하는 프로그램 작성
    N = int(input()) #수열의 길이
    arr = list(map(int, input())) #0과 1로 구성된 수열

    max_len = 0

    count_len = 0
    for i in range(N):
        if arr[i] == 1: #1이면 count_len을 count
            count_len += 1
            #이걸 계속 max_len과 비교하기
            if max_len < count_len:
                max_len = count_len
        else: # arr[i]가 0일 경우
            #그리고 다시 한 번 더 count_len을 max_len에 담아줌으로써 문제 최소화
            if max_len < count_len:
                max_len = count_len
            count_len = 0 #초기화
    print(f'#{tc} {max_len}')