import sys
sys.stdin = open('input4831.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #0번 idx부터 N번 정류장 까지 이동 -> 즉 N+1개의 배열 생성 필요
    #최대 이동 가능 거리 : K
    #충전기가 설치된 M개의 정류장 확인
    K, N, M = map(int, input().split()) #최대 이동 가능 거리, 마지막 정류장 번호, 충전소 개수
    bus_stop = [0] * (N+1)
    check = list(map(int, input().split()))
    for c in check:
        bus_stop[c] += 1
    S = len(bus_stop)
    #print(bus_stop) -> 충전소 위치까지 명확하게 표기함

    idx = 0 #현 index, 현 pos 위치
    charge = 0
    while idx <= N: #마지막 idx의 번호
    # 사실 현재 위치에서 +K만큼 가능하다면 -> 그게 10이거나 10을 초과한다면
    #과감하게 종료
        if idx+K >= N:
            break #도착했으니 빠져나간다.
        #1.현재위치 + K가 == 충전소 위치라면
        if bus_stop[idx+K] == 1: #충전소 위치라면?
            #현재 위치에 현재위치 + K를 대입한다.
            idx = idx + K
            #충전횟수도 증가시킨다.
            charge += 1
            #위에서 조건을 걸어줬지만, 다시 한 번 더
            # 단, 해당 값이 10을 만족시키거나 10을 넘길 경우 종료한다. -> 이미 나는 K만큼 이동할 수 있기 떄문에
            if idx + K >= N:
                break #while문 break
        else:  #2. 현재위치 + K != 충전소 위치라면
            #2-1. 현재 위치 + K에는 없지만 그 범위내에 충전소가 있는경우
            for i in range(K, 0, -1): #3.2.1 이동
                #범위내에 있는 마지막 충전소 위치에 착륙 -> 현재 위치 = 범위 내 마지막 충전소 위치
                #현위치부터 K까지 범위내에서 -> 뒤에서 부터 접근해서 break 건다면 비효율 제거가능
                    #for i in range(K, 0): if arr[i] == K: break
                if idx + i >= N:   # 그리고 if 현재 위치 + i가 10을 만족시키거나 10을 넘길 경우 종료한다. -> 이미 나는 K만큼 이동 가능하기 떄문에
                    break #for문 break
                if bus_stop[idx+i] == 1:
                    idx = idx+i #현재 위치 반영해서
                    charge += 1 #충전 -> 충전횟수를 뺴먹음
                    break
            else:
                # 2-2. 현재 위치 + K 범위 내에도 충전소가 없는 경우
                # 충전횟수 초기화
                charge = 0
                break #while문 종료
    print(f'#{tc} {charge}')


    '''
        #사실 현재 위치에서 +K만큼 가능하다면 -> 그게 10이거나 10을 초과한다면 
    #과감하게 종료
    #1.현재위치 + K가 == 충전소 위치라면
        #현재 위치에 현재위치 + K를 대입한다.
        #충전횟수도 증가시킨다.
            #단, 해당 값이 10을 만족시키거나 10을 넘길 경우 종료한다. -> 이미 나는 K만큼 이동할 수 있기 떄문에
    #2. 현재위치 + K != 충전소 위치라면
        #2-1. 현재 위치 + K에는 없지만 그 범위내에 충전소가 있는경우
            #범위내에 있는 마지막 충전소 위치에 착륙 -> 현재 위치 = 범위 내 마지막 충전소 위치
            #현위치부터 K까지 범위내에서 -> 뒤에서 부터 접근해서 break 건다면 비효율 제거가능
                #for i in range(K, 0): if arr[i] == K: break
                #그리고 if 현재 위치 + i가 10을 만족시키거나 10을 넘길 경우 종료한다. -> 이미 나는 K만큼 이동 가능하기 떄문에 
        #2-2. 현재 위치 + K 범위 내에도 충전소가 없는 경우
            #충전횟수 초기화
    '''