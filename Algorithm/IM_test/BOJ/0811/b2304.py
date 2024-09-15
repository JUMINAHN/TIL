#문어박사 들은 후
import sys
sys.stdin = open('input2304.txt')

box_list = [0] * 1001 #1부터 1000까지니까
box_num = int(input())
for _ in range(box_num):
    L, H = map(int, input().split()) #col의 위치 row의 높이 --> 바닥이 고정되어 있음 --> idx
    box_list[L] = H
#print(box_list) #보면 list가 1부터 1000까지라서 1000개의 범위가 있는데
#여기서 가장 큰 숫자는 뽑을 수 있겠지만,, 가장 맨앞의 숫자와 맨 뒤의 숫자를 어떻게 인지하고 뽑을 수 있을지에 대한 고민이 있음
#list를 채우고 싶어 --> 이전보다 낮으면 나의 값은 필요가 없어
#그러면 일단 기준으로 가장 큰 애의 높이와 idx를 구해보자

#자문제는 가장 높은데까지 어디를 기점으로 시작할 것인가.. 저기 H가 8인 곳을 찾고 싶은데 어떻게 접근해야할지 모르겠다..
#0이 아닌 것중 마지막 list?
#box의 범위
box_range = []
for i in range(len(box_list)):
    if box_list[i] != 0:
        box_range.append(i)
#print(box_range)

max_idx = 0
max_box = 0
for i in range(len(box_list)):
    if box_list[max_idx] < box_list[i]:
        max_idx = i
        max_box = box_list[i]
#print(max_box) #가장 높은 친구의 높이
#print(max_idx) #가장 높은친구의 idx
#i가 i-1보다 작다면 i의 값을 그대로 가져올래요
for i in range(1, max_idx+1): #가장 높은 곳까지
    if box_list[i] < box_list[i-1]:
        box_list[i] = box_list[i-1]
#print(box_list) #원하는대로 나왔습니다.
for i in range(box_range[-1]-1, max_idx, -1):
    if box_list[i] < box_list[i+1]:
        box_list[i] = box_list[i+1] #나보다 나 뒤에있는 것
#print(box_list)
#숫자가 다를 때
count = [0] * 1001
for b in box_list:
    if b == 0 :
        continue
    count[b] += 1
#print(count)
total = 0
for i in range(len(count)):
    if count[i] == 0:
        continue
    total += count[i] * i
print(total)
