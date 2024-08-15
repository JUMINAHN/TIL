import sys

sys.stdin = open('input2.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    route = list(map(int, input().split()))
    core_route = []

    new_list = []
    for i in range(N-1):
        if i == 0:
            new_list.append(route[i]) #원하는 의도 충족
        if route[i] <= route[i+1]: #다음값이 더 크다면 core_route에 저장 #어떻게 1부터 들어가졌지..?
            new_list.append(route[i+1]) #나를 어팬드 해야할 것 같음
        else: #그게 아니라면
            # print(new_list)
            #list로 묶어야 들어간다 *****
            core_route.append(list(new_list))
            new_list.clear()
            new_list.append(route[i+1])
    if len(new_list) > 1:
        core_route.append(new_list)

    if not core_route:
        print(f'#{tc} 0')
    #print(core_route)

    total_scale = 0
    total_length = 0
    main_idx = 0

    for i in range(len(core_route)):
        length = len(core_route[i])
        #문제를 잘 읽자,, 차이를 구하는 것이었따.
        scale = (core_route[i][-1] - core_route[i][0]) // length #경사 완만도 -> length로 진행해야함

        if i == 0: #초기값 설정하고
            total_scale = scale
            total_length = length

        ##여기가 문제가 되는 것 같은데##
        if total_scale > scale: #더 작은 경사도를 넣기 위함
            total_scale = scale
            total_length = length #경사도도 반영하고, 나의 길이도 반영을 같이해줘야함

        elif total_scale == scale :
            if total_length < length: #지금  길이가 더 길다면, 반영하고
                total_length = length
            else :
                pass #아니라면 지금의 길이를 유지하자
    print(f'#{tc} {total_length}') #현재 제일 작은 값들이 들어오고 있음
