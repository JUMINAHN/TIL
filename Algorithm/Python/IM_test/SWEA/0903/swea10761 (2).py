import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    arr = list(input().split()) #현재 작업 정보를 불러오기 위해
    #현재 작업자 정보 저장
    btn_time = arr.pop(0)
    now = {'B': 1, 'O': 1}
    prev_color = 0
    prev_distance = 0
    time = 0  # 시간 증가 확인을 위한 변수 설정
    for i in range(len(arr)//2):
        color, target = arr[i * 2], arr[i * 2 + 1]
        target = int(target)

    # 1. 이전 작업자가 나일 경우
 	#- 현재 작업 정보를 이전 작업에 누적해서 저장한다.
        #             += 이전 작업자 정보를 담는다.
        real_position = now.get(color)
        d = abs(real_position - target)  # ..? #실제이동이 필요한 거리 -> 최족 도착 위치 갱신
        if color == prev_color:
            prev_distance += (d+1)  #버튼 1누를 때도 이동거리 1칸 증가.
            time += d
            now[color] = target  #현재 color 위치 타겟
            time += 1 #버튼 누르기
            #이동 거리만큼 작업 시간
    # > 다른 사람이 이전 작업자라면 : 작업 정보를 갱신해야 한다.
        else: #color != prev_color
    # 2. 이전 작업자가 내가 아닌 경우
            ##현재위치에서 가고자 하는 위치 : distance = 0
        # 	2-1. 이전 작업자가 나보다 이동이 더 많은 경우
        # 이동 거리 와 위치
            if prev_distance >= d:
                #실제 이동 위치 값
                now[color] = target
                #distance = now[color]
            # 	> 조건 : 나보다 이동이  많거나 같은 경우
        # 	- 현재 작업자는 버튼만 누르면 된다.
                time += 1 #버튼을 누를 시 -> 시간 증가 확인
        #             - 이전 작업자 정보를 담는다.
                prev_color = color
                prev_distance = 1
                #prev_distance = d
        # 	2-2. 이전 작업자가 나보다 이동이 더 적은 경우
            else: #prev_distance < distance
        # 	- 현재 작업자는 이전 작업자의 거리 차 만큼 이동하고 버튼을 누른다.
                #target = (d - prev_distance)
                time += (d - prev_distance) #이동한 거리만큼의 시간이 증가
        #             - 이전 작업자 정보를 담는다.
                time += 1 #버튼 누르기
                prev_color = color
                prev_distance = (d - prev_distance + 1) #버튼 1누를 때도 이동거리 1칸 증가.
                now[color] = target #최종 위치
    print(f'#{tc} {time}')