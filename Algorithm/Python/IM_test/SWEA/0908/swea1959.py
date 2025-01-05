import sys

sys.stdin = open('input1959.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #두개의 숫자열 -> 서로 마주보는 위치 변경
    #B의 위치만 계속 바꿔주면 된다.
    N, M =map(int, input().split()) #A와 B의 크기
    small = list(map(int, input().split()))
    large = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        small, large = large, small #무조건적인 위치 바꿔주고

    max_num = 0
    #3개씩 추출해준다.
    for i in range(0, M-N+1): #범위 -> 시작 범위 설정 -> 아 작은 범위에서 큰것으로 뺴줘야하는데 해당 부분 실수
        data = []
        for j in range(i, i+N): #작은것 범위
            #print(large[j])
            data.append(large[j])
        #print(data) #왜 값이 들어가지지 않는지?
        sum = 0
        for k in range(N): #N만큼 검토
            sum += data[k] * small[k] #data에서 뽑은거랑 small 곲하기
        if max_num < sum:
            max_num = sum
    #고정과 이동
    print(f'#{tc} {max_num}') #잘 표기하기 -> 무엇이 무엇인지 구역 잘 나누기


    # print(N)
    # print(M)
    # print(small)
    # print(large)



    # #M을 가장 큰 길이로 맞춰주자. B가 더 긴 길이
    # if large < small and M < N:
    #     large, small = small, large #서로의 위치를 바꿔준다.
    #     M, N = N, M
    # #A의 -> small의 값은 고정
    # #large(B)의 값만 변경
    # max_num = 0
    # for i in range(0, N-M+1): #해당 범위까지
    #     data = []
    #     for j in range(i, i+N): #짧은 길이만큼 -> 바뀌는 범위
    #         data.append(large[j]) #해당 배열을 확인한다.
    #     print(data)

    #print(max_num)

    # 이 배열이랑 기존 배열 곱하기
    # sum = 0
    # for j in range(N):
    #     add = data[j] * small[j]
    #     sum += add
    # if max_num < sum:
    #     max_num = sum