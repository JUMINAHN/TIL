#import sys

#sys.stdin = open('input1206.txt')
#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    N = int(input())
    building = list(map(int, input().split()))

    #조망권 확보가 될 시 변수에 데이터 담기
    total_view = 0
    #조망권 확보를 위해 좌/우 비교
    for i in range(2, N-2): #왜냐하면 N-3의 위치까지 확보해야하기 떄문에
        my_data = building[i]
        another = building[i-2:i] + building[i+1:i+3]
        max_another = max(another)
        if my_data > max_another: #더 크다면
            total_view += (my_data - max_another)
    print(f'#{tc} {total_view}')
