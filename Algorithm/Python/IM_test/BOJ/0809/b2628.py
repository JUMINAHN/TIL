
col, row = map(int, input().split())
try_cut = int(input())

row_box = [0, row] #길이값
col_box = [0, col]

#정렬 -> 선택 정렬 (idx)
def sort_num(box):
    for i in range(len(box) - 1):
        min_idx = i
        for j in range(1 + i, len(box)):
            if box[min_idx] > box[j]:
                min_idx = j
        box[min_idx], box[i] = box[i], box[min_idx]
    return box

#자른값을 넣어줌
for tc in range(1, try_cut+1):
    rc_check, idx = map(int, input().split())
    if rc_check == 0:
        row_box.append(idx)
    else:
        col_box.append(idx)
#print(row_box)

rb = sort_num(row_box)
cb = sort_num(col_box)
#print(rb)
#print(cb)

#종이 각각 잘라내기
max_row = 0
for i in range(1, len(rb)):
   result = row_box[i] - row_box[i-1]
   if max_row < result:
       max_row = result

max_col = 0
for i in range(1, len(cb)):
   result = col_box[i] - col_box[i-1]
   if max_col < result:
       max_col = result

print(max_row * max_col)

