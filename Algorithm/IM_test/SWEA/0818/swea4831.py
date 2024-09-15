import sys

sys.stdin = open('input4831.txt')
#테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    #K:최대이동가능거리, N:종점 정류장번호(N+1)개, M:충전기 개수
    #charge : M 충전기 개수가 위치한 곳
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    #따라서 먼저 전체 정류장을 만든다.
    bus_stop = [0] * (N+1)
    for c in charge : #충전소가 있는 위치를 bus_stop 내부에 반영한다.
        bus_stop[c] = 1 #충전소가 있는 위치는 1로 표기

    i = 0 #i는 현재 위치
    #1. 충전기랑 i+K(충전하고 갈 수 있는 거리)가 같은 위치에 해당 될 경우 계속 직진한다.
    total_charge = 0
    #순회하는 코드를 작성하지 않은 것으로 확인됨, 그럼 i+K가 범위를 초과하지 않는 선에서 for loop
    while i+K <= N:
        if i + K >= N:  # 해당 위치에 도달하게 되면
            break  # 빠져나간다. #디버깅을 통해 위치 잘보기
        if bus_stop[i+K] == 1: #계속해서 이동을 한다.
            i = i + K  # 현재 위치를 충전기 위치로 이동한다.
            total_charge += 1 #해당되는 위치에 와서 충전을 한다.
        #2. 현재 위치랑 충전소가 있는 위치가 다를 경우
        else :
            #충전이 될 것이기 떄문에
            total_charge += 1 #여기서 충전을 하는이유는 순회한만큼 충전이 되는 것을 막기 위함
            # a. 범위안에 충전소가 있는 경우
            #충전기 위치만큼 순회해서, 마지막 충전기 위치 찾기
            for j in range(i+K, i, -1): #i+K만큼의 위치까지 도달해야하기 때문에 #범위때문에 되지 않았던 것이다. 나까지 포함했기 떄문
                if bus_stop[j] == 1:
                    i = j # J를 현재 충전기 위치로 바꾼다.
                    break
            # b. 범위안에 충전소가 없는 경우
            # for- else가 for에 요건이 충족되지 않으면 진행되는게 아니었는가..? -> 맞음 내가 요구하는 조건이 맞았음
            else :
                total_charge = 0
                break

    print(f'#{tc} {total_charge}')

# else:
                # # 전체 충전횟수를 초기화하고 출력한다.
                # # 도착할 수 없는 경우는 0을 출력한다고 했기 때무누에
                #     total_charge = 0
                #     break



