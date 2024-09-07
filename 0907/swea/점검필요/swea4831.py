import sys

sys.stdin = open('../input4831.txt')
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    bus_stop = [0] * (N+1) #충전소 위치가 0부터 N까지기 떄문에
    arr = list(map(int, input().split()))
    for i in range(M):
        bus_stop[arr[i]] += 1 #충전소가 있으면 1표시

    now_idx= 0
    charge = 0
    while now_idx + K <= N : #10을 넘기면 안되기 떄문에 10까지
        if now_idx + K >= N: #정확하게 종점 위치에 도달하면 그냥 나가 충전할 필요도 없어 -> 그리고 종점 위치보다 커도
            break
        #1.현재 위치 + 최대 이동 거리에 충전소가 있다면?
        move_idx = now_idx + K #새로 이동하는 위치
        if bus_stop[move_idx] == 1: #충전소가 있다면
            charge += 1
            now_idx = move_idx #1-1. 현재위치에 이동한 거리로 갱신해주기
            #print(now_idx)

        #2. 현재 위치 + 최대 이동 거리에 충전소가 없다면?
        else:
            temp = now_idx  # 현재 나의 위치를 저장할 것 -> 충전소를 찾지 못했을떄를 대비해서
            move_num = 0
            #2-1. 오는 길에 마주친 가장 마지막 충전소에서 충전 -> `최소`충전
            for i in range(1, K+1): #이동할 것이기 떄문에 1이 최소 K+1이 최대
                if bus_stop[now_idx + i] == 0:
                    move_num = i #나의 위치에 0부터 K만큼 더해진다 -> 맨마지막 i가 더해져서 확인할 것
                #print(now_idx)
            now_idx += move_num #이동되는 거리 -> 여기서 바꼈을 것
            charge += 1
            #자 순회가 끝나고 오는길에 마주한 충전소가 없는지 확인하기 위해 temp로 비교
            if temp == now_idx: #바뀌지 않았다면 일로 들어올 것
                charge = 0 #2-2. 오는 길에 마주친 충전소가 없기 때문에 0을 출력
                break #else-break에 해당이 되지 않는 것인가?
    print(charge)
    '''
    #거리를 지속해서 갱신해줄 것이기 때문에 while문을 사용할 것

    #1.현재 위치 + 최대 이동 거리에 충전소가 있다면?
        #1-1. 현재위치에 이동한 거리로 갱신해주기
    #2. 현재 위치 + 최대 이동 거리에 충전소가 없다면?
        #2-1. 오는 길에 마주친 가장 마지막 충전소에서 충전 -> `최소`충전
            #최소 충전의 요건을 만족시키기 위해선 현 위치에서 이동거리까지의 범위, 뒤에서부터 접근하기
        #2-2. 오는 길에 마주친 충전소가 없기 때문에 0을 출력
    '''