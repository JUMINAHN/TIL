import sys
sys.stdin = open('input2477.txt')
fruit = int(input()) #과일 개수
six = 6 #육각형
bat = []
for _ in range(six):
    direct, distance = map(int, input().split())
    bat.append(distance) #위치 input

max_h = max(bat[0], bat[2], bat[4])
max_w = max(bat[1], bat[3], bat[5])
#print(max_w, max_h) #가장 높은 것 좌우에 있는 것 담기
max_square = max_w * max_h
leftright = [] #대상들 담기
for i in range(six):
    if bat[i] == max_h or bat[i] == max_w:
        leftright.append(bat[(i-1)%six])
        leftright.append(bat[(i+1)%six])
#print
small = 1
for i in range(six):
    if bat[i] not in leftright: #이거 좋았음
        small *= bat[i]
#print(small)
print((max_square-small)*fruit)