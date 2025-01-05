import sys
#전기버스
sys.stdin = open('input4831.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split()) #최대이동거리K, 정류장총개수N, 충전기가 설치도니 M개의 개수
    #정류장 만들기
    bus_stop = [0] * (N+1) #+1을하는 이유는 0부터 시작하기 떄문에 추가로 하나 더 필요하다.
    charge = list(map(int, input().split()))
    for c in charge:
        bus_stop[c] = 1 #충전소가 있음을 나타내기 위해서 0배열에 1을 삽입한다.
    #print(bus_stop)

    idx = 0 #현재 위치
    charge = 0 #충전 횟수를 count하고 싶기 떄문에
    while idx <= N :
#        print(charge)
#         if idx+K == N or idx+K >= N: #더 충전할 필요가 없음 종착지에 도착하여씩 떄문에
#             break #while문 break
#         if idx == N+1 or idx+K > N+1 :
#             break
        if idx + K >= N:
            break
        #print(idx)
        #만약 idx가 N이거나 idx+K가 N보다 커질 경우
        #현재위치 + K가 충전소가 있을 때 계속해서 전진한다.
        if bus_stop[idx+K] == 1: #
            idx = idx + K #이동한 위치를 다시 대입해준다.
            #print(idx)
            charge += 1# 충전한다.
        else: #현재위치에 충전소가 없을 떄 다시 처음으로 돌아가서 가장 마지막에 해당하는 충전소로 간다, 최소 충전을 위해서
            #변하지 않음을 확인하기 위해 잠시 담는다
            # if idx + K >= N:
            #     break
            temp = idx
            charge += 1 #그냥 충전을 한다는 가정을 하고
            result = 0
            for i in range(1, K+1): #k만큼 더해줄 것이기 떄문에
                #print(idx+i)
                # if idx + K == N+1 or idx + K >= N+1:  # 더 충전할 필요가 없음 종착지에 도착하여씩 떄문에
                #     break  # while문 break
                if idx+K<=N and bus_stop[idx+i] == 1: #충전소가 있다면 -> 가장 마지막 충전소 #9-> 14가 바로 적용되어 버리는..
                    result = i #여기서 문제가 발생했고!!
            idx = idx+result #현재의 충전소 위치를 전달해준다. #위치를 잘못 대입한 것을 확인함
            if idx == temp:#여기서 문제가 발생했음
            # else : #다 돌고 조건에 없을 경우를 해야 했음 -> 조건문 설정의 오류, break가 없었기 때문임
                charge = 0
                idx = N + 1 #따라서 그냥 바로 while범위를 벗어나도록 하기 위해서 N보다 1더 크게 설정을 한다.
                break #현재 for i in range의 idx가 끝나버리게됨 그럼 하기에 charge가 카운팅될수도 있는 문제가 발생
    print(f'#{tc} {charge}')