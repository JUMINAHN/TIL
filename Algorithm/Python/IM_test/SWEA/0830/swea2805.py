import sys


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    value = [list(map(int, input())) for _ in range(N)]
    #print(value)
    #value를 받은 것
    #기준점을 기반으로 다시 계산

    standard = N//2
    #기준까지 계산을 한다. 위 아래로 나누어서
    total = 0
    for i in range(0, standard+1): #0부터 순회해야하기 때문에
        #for j in range(0, N): #열을 모두 순회해야함
            for a in value[i][standard-i:standard+i+1]: #i+1해줘야 범위 안에 가능
                total += a
   #print(total)
    for i in range(0, standard): #0부터 순회해야하기 때문에
        #for j in range(0, N): #열을 모두 순회해야함
        #여기 범위를 확인해줘야함
            for a in value[N-1-i][standard-i:standard+i+1]: #i+1해줘야 범위 안에 가능
                total += a
    print(f'#{tc} {total}')


    #아래 계산
    # total2 = 0
    # for i in range(N-1, standard, -1): #역으로 접근
    #     for j in range(0, N):
    #         if value[i][j] in value[i][standard-i:standard+i+1]: #i+1해줘야 범위 안에 가능
    #             total2 += value[N-1-i][j]
    # print(total2)
