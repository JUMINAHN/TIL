import sys

#sys.stdin = open('input2828.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N스크린 크기, M바구니 크기
    screen = [0] * N
    J = int(input()) #사과의 개수
    apple = [0] * J #사과가 떨어지는 위치를 담을 배열
    for i in range(J):
        apple[i] = int(input())
    #나는 일단 0

    move_count = 0 #이동하는 것 카운트할 변수
    apple_count = 0
    bucket_position = 0 #초기값 -> 박스의 크기에 따라 달라짐 #idx기준이기 떄문에

    #바구니 위치, 범위 설정
    #델타처럼 접근을 해야할 것 같기도..?
    while apple_count != J: #apple 개수를 다 세면 종료
        destination = apple[apple_count]-1 #찾을 목적지 (0번쨰 1번쨰 2번쨰) : idx
        #바구니의 범위
        bucket_left = bucket_position #idx
        bucket_right = bucket_position + M - 1 #bucket의 끝 idx

        # 바구니가 목표 위치에 도달할 때까지
        #"사과가 바구니의 범위 밖에 있는 동안" 계속 반복한다는 의미입니다.
        # 즉, 사과가 바구니의 왼쪽 끝보다 왼쪽에 있거나 (destination < bucket_left),
        # 바구니의 오른쪽 끝보다 오른쪽에 있을 때 (destination > bucket_right) 바구니를 이동시킵니다.
        while destination < bucket_left or destination > bucket_right:
        #사과가 바구니의 왼쪽에 있으면 왼쪽으로 이동_왼쪽을 기반으로
            if destination < bucket_left:
                bucket_position -= 1 #bucket 위치변경
                bucket_left -= 1 #bucket 자체가 이동하니까
                bucket_right -= 1
            elif destination > bucket_right: #사과가 바구니의 오른쪽에 있으면 오른쪽으로 이동
                bucket_position += 1
                bucket_left += 1
                bucket_right += 1

            # 벗어나지 않도록 설정
            if bucket_position < 0:  # 0보다 작게된다면 bucket_position은 바구니의 왼쪽 끝 위치입니다.
                bucket_position = 0
                bucket_left = 0
                bucket_right = M - 1
            elif bucket_position + M > N: #bucket_position #바구니의 오른쪽 끝이 화면을 벗어나는지 확인하기 위해서
                #bucket_position + M > N이라면, 바구니의 일부가 화면 오른쪽 끝을 넘어간 것
                bucket_position = N - M
                bucket_left = N - M
                before_right = N -1
            move_count += 1
        apple_count += 1

    print(move_count)