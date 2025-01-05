import sys

sys.stdin = open('input4831.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_idx = list(map(int, input().split()))
    bus_stop = [0] * (N+1)
    for charge in charge_idx:
        bus_stop[charge] = 1
    total_charge = 0

    idx = 0
    while idx+K <= N: #idx 자체는 N만큼 접근하는게 맞다
        if idx+K == N: #마지막 영역에는 충전기가 없기 떄문에 break를 하면 된다
            break

        # 내가 원하는 위치에 충전기가 있다면, K만큼 이동이가능하기 떄문에 해당 부분을 기준점으로 삼음
        if bus_stop[idx+K] == 1:
            total_charge += 1 #충전을 하고
            idx = idx+K #충전된 위치를 반환한다.
        #내가 원하는 위치에 충전기가 없는 경우
        else:
            #경로내에 충전기가 존재하는지 먼저 확인하고, 경로내에 존재한다면 마지막 충전소에서 충전을 한다.
            temp = idx #임시로 현재의 idx를 저장한다.
            for i in range(idx, idx+K+1): #K까지 범위를 확인해야하기 때문에 +1을 해준다.
                if bus_stop[i] == 1:
                    #find_charge = i #그러면 마지막 idx가 담길 것
                    #여기서부터 다시 출발할 것
                    idx = i #마지막 idx를 담을 것


            if idx == temp : #이전이랑 같다면 변함없는 것이니까
                #만약 경로내에 충전기가 존재하지 않는다면 그냥 0을 출력한다.
                total_charge = 0 #충전은 한 번 하지만, 최종적으로 안한거나 마찬가지가 되니까 그냥 0을 출력한다.
                #print(f'#{tc} 0')
                break
            total_charge += 1

    print(f'#{tc} {total_charge}')