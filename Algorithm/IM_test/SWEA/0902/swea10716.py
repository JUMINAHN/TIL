import sys
import copy

sys.stdin = open('input10716.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    arr = list(input().split())
    button = arr.pop(0)
    #편하게 계산하기 위해서 arr // 2한 것만 큼  range를 돌려다시 담는다.

    B = 1 #b를 1로 설정
    O = 2 #orange를 2로 설정

    move_station = [] #누가이동할지, 이동할 거리를 담을 곳
    for i in range(len(arr)//2):
        color = arr[2*i]
        distance = arr[(2*i)+1]
        d_list = [color, int(distance)]
        move_station.append(d_list)
    #일단 bokdo 안에 리스트 하나가 있고 그 리스트에서 0번을 기준으로 특정색깔을 나타내고, 1번을 기준으로 이동거리를 나타낸다.
    #bokdo2 = copy.deepcopy(bokdo1) #bokdo자체를 복사함 -> O를 담을 곳
    move_orange = [0] * 100
    move_blue = [0] * 100
    for mv in move_station:

        mv[0]
        mv[1]