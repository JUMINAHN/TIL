import sys

sys.stdin = open('input2628.txt')
C, R = map(int, input().split())
#가로 C
garo = [0, C]
#세로 R
sero = [0, R]

N = int(input())
for _ in range(N):
    CR, distance = map(int, input().split())
    if CR == 1: #가로
        garo.append(distance)
    else : #세로
        sero.append(distance)
# print(garo)
# print(sero)
garo.sort()
sero.sort()
#가로 세로 sort해주고

max_garo = 0
max_sero = 0
#짜피 지금 다 정렬된 상태
for i in range(len(garo)-1):
    data = garo[i+1] - garo[i]
    if max_garo < data:
        max_garo = data
for i in range(len(sero)-1):
    data = sero[i+1] - sero[i]
    if max_sero < data:
        max_sero = data
# print(max_garo)
# print(max_sero)
#모르겠으면 프린트 찍어보기
print(max_garo * max_sero)