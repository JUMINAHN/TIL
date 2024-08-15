import sys

sys.stdin = open('input2.txt')
# 테스트 케이스 개수
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    route = list(map(int, input().split()))
    core_route = []

    new_list = []
    for i in range(N - 1):
        if i == 0:
            new_list.append(route[i])  # 원하는 의도 충족
        if route[i] <= route[i + 1]:  # 다음 값이 더 크다면
            new_list.append(route[i + 1])
        else:  # 그게 아니라면
            if len(new_list) > 1:  # 단일 요소 리스트는 제외
                core_route.append(list(new_list))
            new_list.clear()
            new_list.append(route[i + 1])
    if len(new_list) > 1:  # 마지막 리스트도 단일 요소인지 확인
        core_route.append(new_list)

    total_scale = float('inf')  # 초기값을 무한대로 설정
    total_length = 0

    for i in range(len(core_route)):
        length = len(core_route[i])
        scale = (core_route[i][-1] - core_route[i][0]) // length  # 경사 완만도

        if total_scale > scale:  # 더 작은 경사도를 넣기 위함
            total_scale = scale
            total_length = length
        elif total_scale == scale:
            if total_length < length:  # 지금 길이가 더 길다면, 반영하고
                total_length = length

    print(f'#{tc} {total_length}')