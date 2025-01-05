import sys
sys.stdin = open("input2304.txt")

box_list = [0] * 1001
box_num = int(input())
for _ in range(box_num):
    L, H = map(int, input().split())
    box_list[L] = H

# 기둥이 있는 위치들만 추출
box_range = [i for i in range(len(box_list)) if box_list[i] != 0]

# 가장 높은 기둥 찾기
max_idx = 0
max_box = 0
for i in box_range:
    if box_list[i] > max_box:
        max_idx = i
        max_box = box_list[i]

# 왼쪽에서 최대 높이 기둥까지 높이 갱신
current_height = 0
for i in range(box_range[0], max_idx + 1):
    if box_list[i] > current_height:
        current_height = box_list[i]
    box_list[i] = current_height

# 오른쪽에서 최대 높이 기둥까지 높이 갱신
current_height = 0
for i in range(box_range[-1], max_idx, -1):
    if box_list[i] > current_height:
        current_height = box_list[i]
    box_list[i] = current_height
print(box_list)

# 면적 계산
area = sum(box_list[i] for i in range(box_range[0], box_range[-1] + 1))
print(area)