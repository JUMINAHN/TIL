import sys

sys.stdin = open('input1206.txt')
#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))

    #조망권 확보를 위한 전체 합산 변수 total
    total = 0

    #list를 순환하면서 나의 높이와 조망권의 차이를 계산할 것
    #좌우로 조망권 2개씩이 확보가 되어야하기 때문에 해당 부분을 잘 확인할 것
    #따라서 나를 기준으로 i-2, i+2가 되어야함 (범위로 따지면 i-2, i+3)
    for i in range(2, N-2): #끝에 최대 2개까지 더 넣어야하기 떄문에, 그림을 그려보면 된다.
        my_height = height[i] #나의 높이 -> 나의 높이는 단순한 idx가 들어감..! --> 변수 오류 (출력을 찍어보면 확인 가능)
        max_height = 0 #조망권 중 가장 높은 높이를 구할 것
        #height 자체를 접근해야 하는데 변수를 잘못 사용함
        jomang = height[i-2:i] + height[i+1:i+3] #'int' object is not subscriptable
        for j in jomang:
            if max_height < j: #여기도 변수 잘못 사용
                max_height = j

        #print(my_height, max_height)
        #조망권의 높이가 가장큰것과 나의 값을 비교한다.
        if my_height > max_height: #만약 내가 더 크다면 나는 조망권을 확보한 것
            total += (my_height - max_height)
        #나보다 크지 않다면 조망권을 확보한것이 아니니까 pass
    print(f'#{tc} {total}')