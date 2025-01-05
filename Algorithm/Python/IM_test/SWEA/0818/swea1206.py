import sys

sys.stdin = open('input1206.txt')
#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    N = int(input()) #건물의 개수
    height = list(map(int, input().split())) #건물의 높이들 나열
    #나를 기준으로 먼저 분리해야 할 것
    #앞에서 2칸 비우기, 뒤에서 두칸 비우기
    total_diff = 0
    for i in range(2, N-2): #N-2까지 해야 N-3이 마지막으로 책정이 됨
        main_height = height[i] #높이들 중 어디를 가르키는가 -> i 번째 범위
        sub_height = height[i-2:i] + height[i+1:i+3] #나눌 범 명확하게 i를 포함시키지 않음
        #sub_height에서 가장 높은 것 계산하기
        max_sub = 0
        for sub in sub_height:
            if max_sub < sub:
                max_sub = sub
        #근데 클 때만 적용이 될 것
        if main_height > max_sub :
            total_diff += main_height - max_sub

    print(f'#{tc} {total_diff}')