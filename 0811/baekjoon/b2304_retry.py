import sys
sys.stdin = open('input2304.txt')

box_count = int(input())
box_list = [0] * 1001
for _ in range(box_count):
    L, H = map(int, input().split())
    box_list[L] = H

#max_num = 0
max_idx = 0
for i in range(len(box_list)): #큰 idx를 구함과 동시에 넣기
    if box_list[max_idx] < box_list[i]:
        max_idx = i
        max_num = box_list[i]
#max까지 왼쪽을 구하고
#left_max = 0
for i in range(1,max_idx+1):
    if box_list[i] < box_list[i-1]:
        box_list[i] = box_list[i-1]
for i in range(len(box_list)-2, max_idx, -1):
    if box_list[i] < box_list[i+1]:
        box_list[i] = box_list[i+1]
#idx와 열값을 그냥 더해
total = 0
for i in range(len(box_list)):
    total += box_list[i]
print(total)