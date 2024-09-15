#종이자르기
C, R = map(int, input().split())
N = int(input())

#선택정렬 실시 -> 갑자기 선택정렬을 못하는 이슈..?
def my_sort(box):
    for i in range(len(box) - 1):
        min_idx = i
        for j in range(i + 1, len(box)):
            if box[min_idx] > box[j]:
                min_idx = j
        box[i], box[min_idx] = box[min_idx], box[i]

def cut_max(box):
    max = 0
    for i in range(len(box)-1):
        if max < box[i+1] - box[i]:
            max = box[i+1] - box[i]
    return max

#가로 박스 / 세로 박스로 나누어 자르기
col_box = [0, C]
row_box = [0, R]

for _ in range(N):
    cr, length = map(int, input().split())
    if cr == 0 :
        row_box.append(length)
    else :
        col_box.append(length)
#sort하고 cut하기
my_sort(col_box)
my_sort(row_box)

#가장 큰 것 도출
col = cut_max(col_box)
row = cut_max(row_box)
print(col * row)