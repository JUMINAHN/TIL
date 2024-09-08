import sys
import copy
sys.stdin = open('../input2477.txt')
fruit = int(input()) #밭의 면적을 구한 후 곱할 것
#6각형
six = 6
line = []
for _ in range(six): #육각형 -> 퐁당 퐁당할 것이라서 direct가 사실 필요없을 것 같음
    direct, distance = map(int, input().split())
    #순서대로 짜피 담긴다.
    line.append(distance)

#print(line)
#가장 긴 것 가로,세로 구분
#뭐가 w,h인지 모르겠지만 일단 격으로 나오는 건 암
max_w = max(line[0], line[2], line[4]) #가장 큰 것 좌우 비교
max_w_i = line.index(max_w)
#print(max_w_i)
max_h = max(line[1], line[3], line[5]) #가장 큰 것 좌우
max_h_i = line.index(max_h)
#print(max_h_i)
square = max_w * max_h
#print(square)

#그래서 idx로 접근해야할 것 같은데
#print(max_h * max_w)
for i in range(six):
    if i == max_w_i: #지금 w와 같다면
        line[i] = 0
        line[(i+1)%six] = 0
        line[(i-1)%six] = 0
    if i == max_h_i : #이전에 만나게 되면 삭제가 됨
        line[i] = 0
        line[(i+1)%six] = 0
        line[(i-1)%six] = 0
small_sq = 1
for i in range(six):
    if line[i] == 0:
        continue
    small_sq *= line[i]
print(fruit*(square - small_sq))