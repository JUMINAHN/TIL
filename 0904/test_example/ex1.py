import sys
#10시 30분 ~ 11시 7분
sys.stdin = open('input1.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #N*N의 크기
    N = int(input())
    #첫줄은 색종이 영역의 크기
    r1,c1,r2,c2 = map(int, input().split()) #1,1,3,4 색칠한 영역만 확인하기
    arr = [list(map(int, input().split())) for _ in range(N)] #잔디에 값을 넣기

    #평탄화 높이의 합
    height_sum =0
    for row in range(r1, r2+1):
        for col in range(c1, c2+1):
            height_sum += arr[row][col]
    #print(height_sum)
    #평탄화 영역의 칸 수
    area_num = (r2-r1+1)*(c2-c1+1)
    #print(area_num)
    aver = height_sum // area_num
    #print(aver)

    #count가 area_num개 만큼 있는지
    #일단 N이 0부터 10까지니까 -> 11개까지 만들어봐
    # #checkpoint의 aver index가 area_num만큼 있으면 되는것아닌가?
    #해당 행위가 반복됨 -> 언제까지? 전체가 모두 2일때까지
    #평탄화 작업
    count = 0 #평탄화작업 몇번?

    check_point = [0] * 11
    while check_point[aver] != area_num:
        check_point = [0] * 11
        max_num = 0
        max_row = 0
        max_col = 0

        min_num = float('inf')
        min_row = float('inf')
        min_col = float('inf')
        #색종이 만큼 돌기
        #가장 작은 값들 담아서
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                num = arr[row][col]
                if max_num < num:
                    max_num = num
                    max_row = row
                    max_col = col
                if min_num > num:
                    min_num = num
                    min_row = row
                    min_col = col
        #가장 큰것 -1
        arr[max_row][max_col] -= 1
        #가장 작은 것 -1
        arr[min_row][min_col] += 1
        count += 1

        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                num = arr[row][col]
                print(num)
                check_point[num] += 1
        print(check_point)
    print(count)

