#내가 생각한 아이디어
#0. 델타를 사용하면 될 것 같음 data_row[1, -1, 0] : 가거나, 뒤로돌아가거나, 멈추거나

#1. move_count == k 만큼 이동
#2. 만약 충전기를 만났을떄 move_count가 0이면 k만큼 move_count 증가
#3. 아니면 일단 남아있는 k만큼 datarow [1] 전진
#4. 2,3조건 외 그냥 전진을 할 때 다음 충전기 위치나 끝까지에 도달하지 못할 경우
#5. 원래 해당했던 i의 조건으로 돌아감 (아니면 없앴던 datarow [-1] 조건 만큼 후진
#6. i조건으로 돌아까게 되면 원래의 move_count 개수만큼 다시 복원을 하고,
#7. 그럼에도 다음 충전기와 끝에 도달하지 못할경우 0을 출력한다.

import sys

sys.stdin = open('input18058.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split()) #K : 이동횟수, N : 총길이, M:충전기 개수
    M_idex = list(map(int, input().split())) #충전기 위치
    #data_column = [1, -1, 0]
    move_count = K
    bus_stop = [0] * (N+1) #정류장 개수
    result_count = 0

    for bus_i in range(N): #bus_stop이 0임 --> i == 0같은 것
        move_count -= 1 #loop가 돌떄마다 -1감소
        for M_p in M_idex: #충전기 위치
            if bus_i == M_p and move_count == 0:
                move_count += K
                result_count += 1
            else :
                break
        if move_count == 0 and bus_i not in M_idex and bus_i != N-1:
            move_count += K
            result_count +=1
            if move_count == 0 and bus_i not in M_idex and bus_i != N-1:
                break

        if move_count == 0:
            break
    print(result_count)
