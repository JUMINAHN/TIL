col, row = map(int, input().split())
col_line = [0, col]
row_line = [0, row]

cut = int(input())
for _ in range(cut):
    rc, line_num = map(int, input().split())
    if rc == 0:
        row_line.append(line_num)
    else :
        col_line.append(line_num)
#정렬 실시 -- idx기준
#col
for i in range(len(col_line)-1):
    min_idx = i
    for j in range(i+1, len(col_line)):
        if col_line[min_idx] > col_line[j]:
            min_idx = j
    col_line[min_idx], col_line[i] = col_line[i], col_line[min_idx]
#row
for i in range(len(row_line)-1):
    min_idx = i
    for j in range(i+1, len(row_line)):
        if row_line[min_idx] > row_line[j]:
            min_idx = j
    row_line[min_idx], row_line[i] = row_line[i], row_line[min_idx]
#print(row_line)
#print(col_line)
#row의 가장 큰 값
max_row = 0
for i in range(1, len(row_line)):
    result = row_line[i] - row_line[i-1]
    if max_row < result:
        max_row = result
max_col = 0
for i in range(1, len(col_line)):
    result = col_line[i] - col_line[i-1]
    if max_col < result:
        max_col = result

print(max_row * max_col)