import sys

sys.stdin = open('input2628.txt')
C, R = map(int, input().split())
cut = int(input())

col_box = [0, R]
row_box = [0, C]

#cut slicing?
for _ in range(cut): #3번이면 3번 진행될 것
    rc, number = map(int, input().split())
    if rc == 0:
        col_box.append(number)
    else :
        row_box.append(number)
#
# print(col_box)
# print(row_box)
#가장 큰 범위의 길이들 추출

#내가 원하는 것을 진행하려면 정렬
col_box.sort()
row_box.sort()


max_row = 0
# print(row_box)
for i in range(1, len(row_box)):
    result = row_box[i] - row_box[i-1]
    if max_row < result:
        max_row = result
    #print('row' , result)

max_col = 0
for i in range(1, len(col_box)):
    result = col_box[i] - col_box[i-1]
    #print(result)
    if max_col < result:
        max_col = result

print(max_row * max_col)